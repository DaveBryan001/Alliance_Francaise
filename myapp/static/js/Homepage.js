 //Get aLL dropdoms from the document 
const dropdowns = document.querySelectorAll('.lang_drop_down');

//Loop through aLL dropdown eLements 
dropdowns.forEach(lang_drop_down => { 
//Get inner eLements from each dropdom 
const select = dropdowns.querySelector('.select'); 
const caret = dropdowns.querySelector('.carets'); 
const menu = dropdowns.querySelector('.menu'); 
const options = dropdowns.querySelectorAll('.menu li'); 
const selected = dropdowns.querySelector('.selected'); 

/*
we are usirrg this method tn order ro hove 
muLtipLe dropdom menus on the page work */

//Add a cLick event to the seLect element
select.addEventListener('click', () => { 
//Add the cLicked select styles to the select 
select.classList.toggle('select-clicked'); 
//Add the rotate styles to the caret element 
caret.classList.toggle('caret-rotate'); 
//Add the opm sty es to tne enu e Lei, nt 
menu.classList.toggle('menu-open');
});


//Loop through ULL option e 
options.forEach(option => { 
//Add 0 cLick event to tr 
option.addEventListener('click', () => { 
//Change selected inner 
selected.innerText = option.innerText; 
//Add the cLicked se Lec 
select.classList.remove('select-clicked');


caret.classList.remove('caret-rotate'); 
//Add the open styLes to the menu eLement 

menu.classList.remove('menu-open'); 
//Remove active cLass frm oLL option element: 
options.forEach(option => {
  option.classList.remove('active');
});

//Add active cLass to clicked option eLemertt 
option.classList.add('active');

    });
  });
});


/* //HUU Lire LLiLneu» e LCLL» Ly Le» Lu ure ae LCLL e Lemerl& 
select. classList. Remve( 'select-clicked '); 

/lAdd the rotate styLes to the caret eLement 
caret. classList. Remove« 'caret-rotate'); 
//Add the open styles to the menu element 

enu. classList. Remove( 'menu-open'); 
{Remove active cLass frm aLL option eLements 

ptions. ForEach(option a> 
option. classList. Remove« 'active' » ;

lAdd active cLass to clicked option eLemertt 
ption. classList. Addi 'active');