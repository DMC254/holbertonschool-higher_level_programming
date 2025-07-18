document.addEventListener('DOMContentLoaded', function() {
    const readHeader = document.getElementById('red_header');

    readHeader.addEventListener('click', function() {
        const header = document.querySelector('header');
        header.style.color = '#FF0000';
    });
});
