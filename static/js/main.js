
document.addEventListener('DOMContentLoaded', () => {

    // MOBILE MENU

    const menuButton = document.getElementById('mobileMenuButton');
    const navLinks = document.querySelector('.nav-links');

    if (menuButton && navLinks) {
        menuButton.addEventListener('click', () => {
            const isOpen = navLinks.classList.toggle('mobile-open');

            menuButton.setAttribute('aria-expanded', String(isOpen));
            menuButton.textContent = isOpen ? '✕' : '☰';
        });
    }


    // FAVORITES

    const getFavorites = () => {
        try {
            return JSON.parse(
                localStorage.getItem('wallpaperFavorites') || '[]'
            );
        } catch {
            return [];
        }
    };

    const saveFavorites = (favorites) => {
        localStorage.setItem(
            'wallpaperFavorites',
            JSON.stringify(favorites)
        );
    };

    const favoriteButtons = document.querySelectorAll(
        '[data-favorite]'
    );

    favoriteButtons.forEach(button => {
        const wallpaperId = Number(button.dataset.favorite);

        const updateButton = () => {
            const isFavorite = getFavorites().includes(wallpaperId);

            button.classList.toggle('is-favorite', isFavorite);
            button.textContent = isFavorite ? '♥' : '♡';
            button.setAttribute('aria-pressed', String(isFavorite));
            button.setAttribute(
                'aria-label',
                isFavorite ? 'Remove from favorites' : 'Add to favorites'
            );
        };

        updateButton();

        button.addEventListener('click', (event) => {
            event.preventDefault();
            event.stopPropagation();

            let favorites = getFavorites();

            if (favorites.includes(wallpaperId)) {
                favorites = favorites.filter(
                    id => id !== wallpaperId
                );
            } else {
                favorites.push(wallpaperId);
            }

            saveFavorites(favorites);
            updateButton();
        });
    });

});
