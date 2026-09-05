/**
 * Fitra Nurmayadi — Technical Portfolio Client Logic
 * Lightweight, zero-bloat, instant client-side filtering and lightbox.
 */

(function () {
    'use strict';

    // State
    let activeCategory = 'all';
    let searchQuery = '';
    let lightboxImages = [];
    let currentLightboxIndex = 0;
    let currentProjectTitle = '';

    // Data Source
    const data = window.PORTFOLIO_DATA || { projects: [], categories: [] };
    const allProjects = data.projects || [];

    // DOM Elements
    const featuredGrid = document.getElementById('featured-grid');
    const projectsGrid = document.getElementById('projects-grid');
    const categoryTabs = document.getElementById('category-tabs');
    const searchInput = document.getElementById('search-input');
    const searchClear = document.getElementById('search-clear');
    const resultsCount = document.getElementById('results-count');
    const themeToggle = document.getElementById('theme-toggle');

    // Lightbox Elements
    const lightboxModal = document.getElementById('lightbox-modal');
    const lightboxBackdrop = document.getElementById('lightbox-backdrop');
    const lightboxClose = document.getElementById('lightbox-close');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxTitle = document.getElementById('lightbox-title');
    const lightboxCounter = document.getElementById('lightbox-counter');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxPrev = document.getElementById('lightbox-prev');
    const lightboxNext = document.getElementById('lightbox-next');

    // Init Theme
    function initTheme() {
        const savedTheme = localStorage.getItem('fn_portfolio_theme');
        if (savedTheme === 'light') {
            document.body.classList.add('light-mode');
        } else {
            document.body.classList.remove('light-mode');
        }

        if (themeToggle) {
            themeToggle.addEventListener('click', () => {
                document.body.classList.toggle('light-mode');
                const isLight = document.body.classList.contains('light-mode');
                localStorage.setItem('fn_portfolio_theme', isLight ? 'light' : 'dark');
            });
        }
    }

    // Render Featured Cards (Flagship Research)
    function renderFeaturedProjects() {
        if (!featuredGrid) return;
        const featured = allProjects.filter(p => p.featured);

        featuredGrid.innerHTML = featured.map(p => {
            const hasImages = p.images && p.images.length > 0;
            const primaryImage = hasImages ? p.images[0] : '';
            const mediaCountBadge = hasImages && p.images.length > 1 ? `<span class="media-badge">${p.images.length} Figures</span>` : '';

            const hardwarePills = (p.hardware || []).map(h => `<span class="pill">${escapeHtml(h)}</span>`).join('');
            const stackPills = (p.stack || []).map(s => `<span class="pill">${escapeHtml(s)}</span>`).join('');

            return `
                <article class="featured-card" data-project-id="${p.id}">
                    ${hasImages ? `
                    <div class="featured-media" data-project-id="${p.id}">
                        <img src="${primaryImage}" alt="${escapeHtml(p.title)}" loading="lazy">
                        ${mediaCountBadge}
                    </div>
                    ` : ''}
                    <div class="featured-body">
                        <div class="card-topline">
                            <span class="category-tag">${escapeHtml(p.category)}</span>
                            <span class="year-tag">${p.year}</span>
                        </div>
                        <h3 class="featured-title">
                            <a href="${p.github_url}" target="_blank" rel="noopener">${escapeHtml(p.title)} &rarr;</a>
                        </h3>
                        <p class="featured-summary">${escapeHtml(p.summary)}</p>
                        
                        <div class="metric-box">
                            <strong>Benchmark & Architecture:</strong> ${escapeHtml(p.metrics)}
                        </div>

                        <div class="hardware-pills">
                            ${hardwarePills}
                            ${stackPills}
                        </div>

                        <div class="card-actions">
                            <a href="${p.github_url}" target="_blank" rel="noopener" class="btn-action primary">
                                <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                                    <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z"/>
                                </svg>
                                <span>GitHub Repository</span>
                            </a>
                            ${hasImages ? `
                            <button type="button" class="btn-action view-gallery-btn" data-project-id="${p.id}">
                                <span>View Figures (${p.images.length})</span>
                            </button>
                            ` : ''}
                        </div>
                    </div>
                </article>
            `;
        }).join('');

        // Attach image click events
        featuredGrid.querySelectorAll('.featured-media, .view-gallery-btn').forEach(el => {
            el.addEventListener('click', (e) => {
                const projectId = el.getAttribute('data-project-id');
                openProjectGallery(projectId);
            });
        });
    }

    // Render Category Tabs
    function renderCategoryTabs() {
        if (!categoryTabs) return;
        const categories = data.categories || [
            { id: 'all', name: 'All Work', count: allProjects.length }
        ];

        categoryTabs.innerHTML = categories.map(cat => {
            const count = cat.id === 'all' 
                ? allProjects.length 
                : allProjects.filter(p => p.category_id === cat.id).length;

            return `
                <button class="tab-btn ${cat.id === activeCategory ? 'active' : ''}" data-category="${cat.id}">
                    <span>${escapeHtml(cat.name)}</span>
                    <span class="tab-count">[${count}]</span>
                </button>
            `;
        }).join('');

        categoryTabs.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                activeCategory = btn.getAttribute('data-category');
                categoryTabs.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                filterAndRenderProjects();
            });
        });
    }

    // Filter and Render Projects Grid
    function filterAndRenderProjects() {
        if (!projectsGrid) return;

        const query = searchQuery.trim().toLowerCase();

        const filtered = allProjects.filter(p => {
            // Category check
            const matchesCat = activeCategory === 'all' || p.category_id === activeCategory;
            if (!matchesCat) return false;

            // Search query check
            if (!query) return true;

            const searchable = [
                p.title,
                p.summary,
                p.category,
                p.metrics,
                ...(p.hardware || []),
                ...(p.stack || []),
                p.year
            ].join(' ').toLowerCase();

            return searchable.includes(query);
        });

        // Update count
        if (resultsCount) {
            resultsCount.textContent = `Showing ${filtered.length} of ${allProjects.length} projects`;
        }

        if (filtered.length === 0) {
            projectsGrid.innerHTML = `
                <div class="empty-state">
                    <p>No matching projects found for "<strong>${escapeHtml(searchQuery)}</strong>" in this category.</p>
                </div>
            `;
            return;
        }

        projectsGrid.innerHTML = filtered.map(p => {
            const hasImages = p.images && p.images.length > 0;
            const tags = [...(p.hardware || []), ...(p.stack || [])].slice(0, 5);

            return `
                <article class="project-card">
                    <div class="project-header">
                        <span class="project-cat">${escapeHtml(p.category)}</span>
                        <span class="project-year">${p.year}</span>
                    </div>

                    <h4 class="project-title">
                        <a href="${p.github_url}" target="_blank" rel="noopener">${escapeHtml(p.title)} &rarr;</a>
                    </h4>

                    <p class="project-desc">${escapeHtml(p.summary)}</p>

                    <div class="project-metric">
                        <strong>Architecture:</strong> ${escapeHtml(p.metrics)}
                    </div>

                    <div class="project-tags">
                        ${tags.map(t => `<span class="pill">${escapeHtml(t)}</span>`).join('')}
                    </div>

                    <div class="project-footer">
                        <a href="${p.github_url}" target="_blank" rel="noopener" class="btn-action">
                            <span>Repository &rarr;</span>
                        </a>

                        ${hasImages ? `
                        <button type="button" class="btn-action view-gallery-btn" data-project-id="${p.id}">
                            <span>Figures (${p.images.length})</span>
                        </button>
                        ` : ''}
                    </div>
                </article>
            `;
        }).join('');

        // Attach click listener for gallery buttons
        projectsGrid.querySelectorAll('.view-gallery-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const projectId = btn.getAttribute('data-project-id');
                openProjectGallery(projectId);
            });
        });
    }

    // Search Input Handling
    function initSearch() {
        if (!searchInput) return;

        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value;
            if (searchClear) {
                searchClear.style.display = searchQuery ? 'block' : 'none';
            }
            filterAndRenderProjects();
        });

        if (searchClear) {
            searchClear.addEventListener('click', () => {
                searchInput.value = '';
                searchQuery = '';
                searchClear.style.display = 'none';
                searchInput.focus();
                filterAndRenderProjects();
            });
        }
    }

    // Lightbox Gallery Management
    function openProjectGallery(projectId) {
        const project = allProjects.find(p => p.id === projectId);
        if (!project || !project.images || project.images.length === 0) return;

        lightboxImages = project.images;
        currentLightboxIndex = 0;
        currentProjectTitle = project.title;

        updateLightbox();
        if (lightboxModal) {
            lightboxModal.classList.add('open');
            lightboxModal.setAttribute('aria-hidden', 'false');
            document.body.style.overflow = 'hidden';
        }
    }

    function closeLightbox() {
        if (!lightboxModal) return;
        lightboxModal.classList.remove('open');
        lightboxModal.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
    }

    function updateLightbox() {
        if (!lightboxImg || lightboxImages.length === 0) return;

        const currentPath = lightboxImages[currentLightboxIndex];
        lightboxImg.src = currentPath;

        if (lightboxTitle) {
            lightboxTitle.textContent = currentProjectTitle;
        }

        if (lightboxCounter) {
            lightboxCounter.textContent = `${currentLightboxIndex + 1} / ${lightboxImages.length}`;
        }

        if (lightboxCaption) {
            const fileName = currentPath.split('/').pop().replace(/[-_]/g, ' ').replace(/\.[^/.]+$/, '');
            lightboxCaption.textContent = `${fileName} (Documentation & Figure)`;
        }

        if (lightboxPrev) {
            lightboxPrev.style.display = lightboxImages.length > 1 ? 'flex' : 'none';
        }
        if (lightboxNext) {
            lightboxNext.style.display = lightboxImages.length > 1 ? 'flex' : 'none';
        }
    }

    function initLightbox() {
        if (!lightboxModal) return;

        if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
        if (lightboxBackdrop) lightboxBackdrop.addEventListener('click', closeLightbox);

        if (lightboxPrev) {
            lightboxPrev.addEventListener('click', () => {
                currentLightboxIndex = (currentLightboxIndex - 1 + lightboxImages.length) % lightboxImages.length;
                updateLightbox();
            });
        }

        if (lightboxNext) {
            lightboxNext.addEventListener('click', () => {
                currentLightboxIndex = (currentLightboxIndex + 1) % lightboxImages.length;
                updateLightbox();
            });
        }

        window.addEventListener('keydown', (e) => {
            if (!lightboxModal.classList.contains('open')) return;

            if (e.key === 'Escape') {
                closeLightbox();
            } else if (e.key === 'ArrowLeft' && lightboxImages.length > 1) {
                currentLightboxIndex = (currentLightboxIndex - 1 + lightboxImages.length) % lightboxImages.length;
                updateLightbox();
            } else if (e.key === 'ArrowRight' && lightboxImages.length > 1) {
                currentLightboxIndex = (currentLightboxIndex + 1) % lightboxImages.length;
                updateLightbox();
            }
        });
    }

    // Helper: Escape HTML
    function escapeHtml(str) {
        if (!str) return '';
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#039;');
    }

    // DOM Ready Initialization
    document.addEventListener('DOMContentLoaded', () => {
        initTheme();
        renderFeaturedProjects();
        renderCategoryTabs();
        filterAndRenderProjects();
        initSearch();
        initLightbox();
    });

})();
