document.addEventListener('DOMContentLoaded', () => {
    // State variables
    let allProjects = [];
    let activeCategory = 'all';
    let searchQuery = '';
    let currentCarouselIndex = 0;
    let currentCarouselImages = [];

    // DOM Elements
    const projectsGrid = document.getElementById('projects-grid');
    const searchInput = document.getElementById('search-input');
    const searchClearBtn = document.getElementById('search-clear-btn');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const themeToggleBtn = document.getElementById('theme-toggle');
    const projectModal = document.getElementById('project-modal');
    const modalCloseBtn = document.getElementById('modal-close-btn');

    // Modal Info Elements
    const modalTitle = document.getElementById('modal-project-title');
    const modalCategory = document.getElementById('modal-project-category');
    const modalDescription = document.getElementById('modal-project-description');
    const modalLinks = document.getElementById('modal-project-links');

    // Carousel Elements
    const carouselSlides = document.getElementById('carousel-slides');
    const carouselDots = document.getElementById('carousel-dots');
    const carouselPrevBtn = document.getElementById('carousel-prev-btn');
    const carouselNextBtn = document.getElementById('carousel-next-btn');

    // ==========================================================================
    // THEME TOGGLE (DARK / LIGHT MODE)
    // ==========================================================================
    const savedTheme = localStorage.getItem('portfolio-theme') || 'dark';
    if (savedTheme === 'light') {
        document.body.classList.remove('dark-mode');
        document.body.classList.add('light-mode');
        themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
    } else {
        document.body.classList.remove('light-mode');
        document.body.classList.add('dark-mode');
        themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
    }

    themeToggleBtn.addEventListener('click', () => {
        if (document.body.classList.contains('dark-mode')) {
            document.body.classList.remove('dark-mode');
            document.body.classList.add('light-mode');
            themeToggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
            localStorage.setItem('portfolio-theme', 'light');
        } else {
            document.body.classList.remove('light-mode');
            document.body.classList.add('dark-mode');
            themeToggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
            localStorage.setItem('portfolio-theme', 'dark');
        }
    });

    // ==========================================================================
    // FETCH DATA & INITIATE
    // ==========================================================================
    async function loadProjects() {
        try {
            const response = await fetch('./projects.json');
            if (!response.ok) {
                throw new Error('Gagal mengambil data proyek.');
            }
            allProjects = await response.json();
            const countEl = document.getElementById('stats-projects-count');
            if (countEl) countEl.textContent = allProjects.length;
            renderProjects();
        } catch (error) {
            console.error('Error loading projects:', error);
            projectsGrid.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-exclamation-triangle" style="color: #ef4444;"></i>
                    <h3>Gagal Memuat Data</h3>
                    <p>Pastikan file <code>projects.json</code> sudah digenerate dengan menjalankan skrip migrasi.</p>
                </div>
            `;
        }
    }

    // ==========================================================================
    // RENDER PROJECTS GRID
    // ==========================================================================
    function renderProjects() {
        // Filter projects based on category and search query
        const filtered = allProjects.filter(project => {
            const matchesCategory = activeCategory === 'all' || project.category === activeCategory;
            
            const matchesSearch = searchQuery === '' || 
                project.title.toLowerCase().includes(searchQuery) ||
                project.category.toLowerCase().includes(searchQuery) ||
                project.description_paragraphs.some(p => p.toLowerCase().includes(searchQuery));
                
            return matchesCategory && matchesSearch;
        });

        // Clear loading or existing cards
        projectsGrid.innerHTML = '';

        if (filtered.length === 0) {
            projectsGrid.innerHTML = `
                <div class="empty-state">
                    <i class="fas fa-search"></i>
                    <h3>Proyek Tidak Ditemukan</h3>
                    <p>Tidak ada proyek yang cocok dengan kata kunci pencarian atau kategori ini.</p>
                </div>
            `;
            return;
        }

        // Generate cards
        filtered.forEach(project => {
            const card = document.createElement('div');
            card.className = 'project-card';
            
            // Thumbnail image: use the first image if available, else show fallback
            let headerHTML = '';
            if (project.images && project.images.length > 0) {
                headerHTML = `
                    <div class="card-header">
                        <span class="card-tag">${project.category}</span>
                        <img src="${project.images[0]}" alt="${project.title}" class="card-image" loading="lazy">
                    </div>
                `;
            } else {
                headerHTML = `
                    <div class="card-header">
                        <span class="card-tag">${project.category}</span>
                        <div class="card-image-fallback">
                            <i class="fas fa-microchip"></i>
                            <span style="font-size: 0.8rem; font-weight: 600;">No Image / Schematics</span>
                        </div>
                    </div>
                `;
            }

            // Description preview (first paragraph or text preview)
            const previewText = project.description_paragraphs.length > 0 
                ? project.description_paragraphs[0] 
                : 'Merancang sistem embedded dan antarmuka pemrograman.';

            // Links icons
            let linksHTML = '';
            if (project.github_links && project.github_links.length > 0) {
                linksHTML = project.github_links.map(link => `
                    <a href="${link}" target="_blank" class="card-link-icon" title="Lihat Kode di GitHub">
                        <i class="fab fa-github"></i>
                    </a>
                `).join('');
            }

            card.innerHTML = `
                ${headerHTML}
                <div class="card-body">
                    <h3>${project.title}</h3>
                    <p>${previewText}</p>
                    <div class="card-footer">
                        <button class="card-btn detail-btn" data-id="${project.id}">Lihat Detail</button>
                        <div class="card-links">
                            ${linksHTML}
                        </div>
                    </div>
                </div>
            `;

            // Bind click for open detail button
            card.querySelector('.detail-btn').addEventListener('click', () => {
                openProjectModal(project);
            });
            
            projectsGrid.appendChild(card);
        });
    }

    // ==========================================================================
    // FILTER & SEARCH HANDLERS
    // ==========================================================================
    // Filter Tabs click
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            filterBtns.forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            activeCategory = e.target.getAttribute('data-category');
            renderProjects();
        });
    });

    // Search input typing
    searchInput.addEventListener('input', (e) => {
        searchQuery = e.target.value.toLowerCase().strip();
        if (searchQuery !== '') {
            searchClearBtn.style.display = 'block';
        } else {
            searchClearBtn.style.display = 'none';
        }
        renderProjects();
    });

    // Clear search
    searchClearBtn.addEventListener('click', () => {
        searchInput.value = '';
        searchQuery = '';
        searchClearBtn.style.display = 'none';
        renderProjects();
        searchInput.focus();
    });

    // String trim polyfill if needed
    if (!String.prototype.strip) {
        String.prototype.strip = function() {
            return this.replace(/^\s+|\s+$/g, '');
        };
    }

    // ==========================================================================
    // MODAL DIALOG & CAROUSEL GALLERY
    // ==========================================================================
    function openProjectModal(project) {
        // Set info
        modalTitle.textContent = project.title;
        modalCategory.textContent = project.category;
        
        // Render description paragraphs
        modalDescription.innerHTML = project.description_paragraphs.map(p => `<p>${p}</p>`).join('');

        // Render github links
        if (project.github_links && project.github_links.length > 0) {
            modalLinks.innerHTML = `
                <a href="${project.github_links[0]}" target="_blank" class="btn-github">
                    <i class="fab fa-github"></i> Lihat Kode di GitHub
                </a>
            `;
        } else {
            modalLinks.innerHTML = '';
        }

        // Setup Carousel Images
        currentCarouselImages = project.images || [];
        currentCarouselIndex = 0;

        setupCarousel();

        // Open Overlay
        projectModal.classList.add('open');
        document.body.style.overflow = 'hidden'; // Lock page scroll
    }

    function closeProjectModal() {
        projectModal.classList.remove('open');
        document.body.style.overflow = ''; // Unlock page scroll
    }

    modalCloseBtn.addEventListener('click', closeProjectModal);
    
    // Close modal when clicking on backdrop overlay
    projectModal.addEventListener('click', (e) => {
        if (e.target === projectModal) {
            closeProjectModal();
        }
    });

    // Escape key to close modal
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && projectModal.classList.contains('open')) {
            closeProjectModal();
        }
    });

    // Carousel Setup Logic
    function setupCarousel() {
        carouselSlides.innerHTML = '';
        carouselDots.innerHTML = '';

        if (currentCarouselImages.length === 0) {
            // Show fallback image inside carousel if none
            carouselSlides.innerHTML = `
                <div class="carousel-slide active">
                    <div class="card-image-fallback" style="height: 100%; width: 100%;">
                        <i class="fas fa-microchip" style="font-size: 4rem;"></i>
                        <span style="font-weight: 600;">No images or schematics available</span>
                    </div>
                </div>
            `;
            carouselPrevBtn.style.display = 'none';
            carouselNextBtn.style.display = 'none';
            return;
        }

        // Show navigation if more than 1 image
        if (currentCarouselImages.length > 1) {
            carouselPrevBtn.style.display = 'flex';
            carouselNextBtn.style.display = 'flex';
        } else {
            carouselPrevBtn.style.display = 'none';
            carouselNextBtn.style.display = 'none';
        }

        // Generate slides and indicators
        currentCarouselImages.forEach((imgSrc, idx) => {
            const slide = document.createElement('div');
            slide.className = `carousel-slide ${idx === 0 ? 'active' : ''}`;
            slide.innerHTML = `<img src="${imgSrc}" alt="Gambar Proyek" loading="lazy">`;
            carouselSlides.appendChild(slide);

            if (currentCarouselImages.length > 1) {
                const dot = document.createElement('span');
                dot.className = `carousel-dot ${idx === 0 ? 'active' : ''}`;
                dot.addEventListener('click', () => {
                    goToSlide(idx);
                });
                carouselDots.appendChild(dot);
            }
        });
    }

    function goToSlide(index) {
        const slides = document.querySelectorAll('.carousel-slide');
        const dots = document.querySelectorAll('.carousel-dot');

        if (slides.length === 0) return;

        // Reset active classes
        slides[currentCarouselIndex].classList.remove('active');
        if (dots.length > 0) dots[currentCarouselIndex].classList.remove('active');

        // Set index bounds
        currentCarouselIndex = (index + slides.length) % slides.length;

        // Apply active classes
        slides[currentCarouselIndex].classList.add('active');
        if (dots.length > 0) dots[currentCarouselIndex].classList.add('active');
    }

    // Prev / Next button listeners
    carouselPrevBtn.addEventListener('click', () => {
        goToSlide(currentCarouselIndex - 1);
    });

    carouselNextBtn.addEventListener('click', () => {
        goToSlide(currentCarouselIndex + 1);
    });

    // Keyboard arrow keys navigation for carousel inside modal
    document.addEventListener('keydown', (e) => {
        if (projectModal.classList.contains('open') && currentCarouselImages.length > 1) {
            if (e.key === 'ArrowLeft') {
                goToSlide(currentCarouselIndex - 1);
            } else if (e.key === 'ArrowRight') {
                goToSlide(currentCarouselIndex + 1);
            }
        }
    });

    // Start fetching
    loadProjects();
});
