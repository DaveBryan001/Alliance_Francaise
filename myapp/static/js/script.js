document.addEventListener('DOMContentLoaded', function (){
    const langBtn = document.getElementById('lang-btn');
    const langDropdown = document.getElementById('lang-dropdown');
    const selectedLang = document.getElementById('selected-lang');
    
    langBtn.addEventListener('click', function (){
        langDropdown.style.display = langDropdown.style.display === 'block' ? 'none' : 'block';
    });

    langDropdown.addEventListener('click', function(e){
        if (e.target.tagName === 'LI') {
            selectedLang.textContent = e.target.textContent;
            langDropdown.style.display = 'none';
        }
    });

    document.addEventListener('click', function(e){
        if (!langBtn.contains(e.target) && !langDropdown.contains(e.target)){
            langDropdown.style.display = 'none';
        }
    });
});