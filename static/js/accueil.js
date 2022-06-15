// recherche nav

const searchBar = document.getElementById('search-bar-id');
const searchBarInput = document.querySelectorAll('.search-bar-input');
// const searchBarInput = document.getElementById('search-bar-input');
// const searchBarInput2 = document.getElementById('search-bar-input-2');
const searchNavId = document.getElementById('searchNavId');
const toSearchProject = document.querySelectorAll('.to-search-project');

// sidebar
const menuItems = document.querySelectorAll('.menu-item');

// discussions
const discNotification = document.getElementById('messages-notifications');
// const notifPopup = document.querySelector('.notifications-popup');
const discussion = document.querySelectorAll('.discussion');

// modal discussion
const discussionMod = document.querySelectorAll('.discussionMod');
const discussionInfoMod = document.querySelectorAll('.discussionMod .info');
const discSend = document.querySelectorAll('.disc-send');

// commentaires
const iconToggleComments = document.querySelectorAll('.icon-toggle-comments');
const toggleComments = document.querySelectorAll('.toggle-comments');
const listComments = document.querySelectorAll('.list-comments');
const btnReplyComment = document.querySelectorAll('.btn-reply-comment');
const replyComment = document.querySelectorAll('.reply-comment');

// catégories
const category = document.querySelectorAll('.project-line');
const categorySearch = document.getElementById('category-search');

// theme
const theme = document.getElementById('theme');
const themeModal = document.querySelector('.customize-theme');
const fontSizes = document.querySelectorAll('.choose-size span');
var root = document.querySelector(':root');
const colorPalette = document.querySelectorAll('.choose-color span');
const bgPalette = document.querySelectorAll('.choose-bg .bg');
const Bg1 = document.querySelector('.bg-1');
const Bg2 = document.querySelector('.bg-2');
const Bg3 = document.querySelector('.bg-3');


// ================ RECHERCHE NAV ============

// searchBar.addEventListener("click", () =>{
    // searchNavId.classList.toggle('active');
//     searchNavId.style.display = "block";
// })
window.addEventListener('click', function(e){
    if(searchNavId.contains(e.target) || searchBar.contains(e.target)){
        // alert("ok");
        searchNavId.style.display = "block";
        toSearchProject.forEach(pro =>{
            pro.style.display = "none";
        })
    }else{
        // alert("cache");
        searchNavId.style.display = "none";
    }
})

// searches project
// function searchProject(i){
    // const val = searchBarInput[i].value.toLowerCase();
    // console.log(val);
    // if(val === ""){
        
    // }else{
    //     toSearchProject.forEach(pro =>{
    //         pro.style.display = "none";
    //         let name = pro.querySelector('a span h3 span').textContent.toLowerCase();
    //         let title = pro.querySelector('a span h5').textContent.toLowerCase();
    //         if(name.indexOf(val) != -1 || title.indexOf(val) != -1){
    //             pro.style.display = "block";
    //         }else{
    //             pro.style.display = "none";
    //         }
    //     })
    // }
// }

// search projects
for (let i = 0; i < searchBarInput.length; i++) {
    searchBarInput[i].addEventListener('keyup', () => {
        // alert(i)
        const val = searchBarInput[i].value.toLowerCase();
        console.log(val);
        if(val === ""){
            
        }else{
            toSearchProject.forEach(pro =>{
                pro.style.display = "none";
                let name = pro.querySelector('a span h3 span').textContent.toLowerCase();
                let title = pro.querySelector('a span h5').textContent.toLowerCase();
                if(name.indexOf(val) != -1 || title.indexOf(val) != -1){
                    pro.style.display = "block";
                }else{
                    pro.style.display = "none";
                }
            })
        }
    });
    
}
// searchBarInput.addEventListener('keyup', searchProject);



// ============ SIDEBAR ===============

// remove active class from all menu items
const changeActiveItem = () =>{
    menuItems.forEach(item => {
            item.classList.remove('active');
    })
}

menuItems.forEach(item => {
    item.addEventListener('click', ()=>{
        changeActiveItem();
        item.classList.add('active');
    })
})

// notifPopup.style.display  = "none";
window.addEventListener('click', function(e){
    if(document.getElementById('notifications').contains(e.target)){
        document.querySelector('#notifications .notifications-count').style.display = "none";
        document.querySelector('.notifications-popup').style.display  = "block";
    } else{
        document.querySelector('.notifications-popup').style.display  = "none";
    }
})


// ============ end SIDEBAR ===============


// =============== discussions =============

discNotification.addEventListener('click', () =>{
    discNotification.querySelector('.notifications-count').style.display = "none";

})


// ================ discussion modal ====================

// hidden active class from all menu items
// const hiddenDisc = () =>{
//     discussionMod.forEach(item => {
//         item.classList.toggle('hidenn');
//     })
// }

// for (let i = 0; i < discussionInfoMod.length; i++) {
//     discussionInfoMod[i].addEventListener("click", () => {
//         hiddenDisc();
//         discussionMod[i].classList.toggle('hidenn');
//         discussionMod[i].classList.toggle('active');
//         discSend[i].classList.toggle('active');
//     });
    
// }



// =============== end discussions ================


// ================== COMMENTAIRES ======================

const affCachComments = () =>{

}

// toggle list comments

for (let i = 0; i < toggleComments.length; i++) {
    toggleComments[i].addEventListener("click", () => {
        listComments[i].classList.toggle('active');
    });
}
for (let i = 0; i < iconToggleComments.length; i++) {
    iconToggleComments[i].addEventListener("click", () => {
        listComments[i].classList.toggle('active');
    });
}

// toggle reply input for a comment

for (let i = 0; i < btnReplyComment.length; i++) {
    btnReplyComment[i].addEventListener("click", () => {
        replyComment[i].classList.toggle('active');
    });
}




// ============== SEARCH CATEGORIE ===============


// searches chats
const searchCategory = () =>{
    const val = categorySearch.value.toLowerCase();
    // console.log(val);
    category.forEach(cat =>{
        let name = cat.querySelector('h5').textContent.toLowerCase();
        // console.log(name);
        if(name.indexOf(val) != -1){
            cat.style.display = "flex";
        }else{
            cat.style.display = "none";
        }
    })
}

// search searchCategory
categorySearch.addEventListener('keyup', searchCategory);



// ====================== THEME CUSTOMIZATION ==========================

// open modal
const openThemeModal = () =>{
    themeModal.style.display = "grid";
}

// close modal
const closeThemModal = (e) =>{
    if(e.target.classList.contains('customize-theme')){
        themeModal.style.display = "none";
    }
}

document.getElementById('close_modal').addEventListener('click', () =>{
    themeModal.style.display = "none";
})

themeModal.addEventListener('click', closeThemModal)
theme.addEventListener('click', openThemeModal);


//  ============== fonts sizes ===============

// remove active class from spans font size
const removeSizeSelector = () =>{
    fontSizes.forEach(size =>{
        size.classList.remove('active');
    })
}

fontSizes.forEach(size =>{
    size.addEventListener('click', () =>{
        removeSizeSelector();
        let fontSize;
        size.classList.toggle('active');

        if(size.classList.contains('font-size-1')){
            fontSize = '10px';
            root.style.setProperty('----sticky-top-left', '5.4rem')
            root.style.setProperty('----sticky-top-right', '5.4rem')
        } else if(size.classList.contains('font-size-2')){
            fontSize = '13px';
            root.style.setProperty('----sticky-top-left', '5.4rem')
            root.style.setProperty('----sticky-top-right', '-7rem')
        }else if(size.classList.contains('font-size-3')){
            fontSize = '16px';
            root.style.setProperty('----sticky-top-left', '-2rem')
            root.style.setProperty('----sticky-top-right', '-17rem')
        }else if(size.classList.contains('font-size-4')){
            fontSize = '19px';
            root.style.setProperty('----sticky-top-left', '-5rem')
            root.style.setProperty('----sticky-top-right', '-25rem')
        }

        // change font size of the root html element
        document.querySelector('html').style.fontSize = fontSize;
    })

})


// ============ COULEURS ===========

// remove active class from spans font size
const removeColorSelector = () =>{
    colorPalette.forEach(color =>{
        color.classList.remove('active');
    })
}

colorPalette.forEach(color =>{
    color.addEventListener('click', () =>{
        removeColorSelector();
        color.classList.toggle('active');

        if(color.classList.contains('color-1')){
            // primaryHue = 216;
            hue_1 = 216;
            hue_2 = '90%'
            hue_3 = '44%';
        } else if(color.classList.contains('color-2')){
            hue_1 = 27;
            hue_2 = '100%';
            hue_3 = '59%';
        } else if(color.classList.contains('color-3')){
            hue_1 = 347;
            hue_2 = '100%';
            hue_3 = '50%';
        } else if(color.classList.contains('color-4')){
            hue_1 = 120;
            hue_2 = '95%';
            hue_3 = '40%';
        }

        // root.style.setProperty('--primary-color-hue', primaryHue);
        root.style.setProperty('--color-hue_1', hue_1);
        root.style.setProperty('--color-hue_2', hue_2);
        root.style.setProperty('--color-hue_3', hue_3);
    })
})


// ============== WALLPAPER =================


let whiteColorLightness;
let lightColorLightness;
let darkColorLightness;

// change background color
const changeBG = () =>{
    root.style.setProperty('--color-white-lightness', whiteColorLightness);
    root.style.setProperty('--color-light-lightness', lightColorLightness);
    root.style.setProperty('--color-dark-lightness', darkColorLightness);
}

// remove active class
const removeBgSelector = () =>{
    bgPalette.forEach(bg =>{
        bg.classList.remove('active');
    })
}

Bg1.addEventListener('click', () =>{
    removeBgSelector();
    Bg1.classList.toggle('active');

    whiteColorLightness = '100%';
    lightColorLightness = '95%';
    darkColorLightness = '17%';

    changeBG();

    // Bg1.classList.add('active');
    // Bg2.classList.remove('active');
    // Bg3.classList.remove('active');

    // window.location.reload();
})

Bg2.addEventListener('click', () =>{
    removeBgSelector();
    Bg2.classList.toggle('active');

    whiteColorLightness = '20%';
    lightColorLightness = '15%';
    darkColorLightness = '95%';

    // Bg2.classList.add('active');
    // Bg1.classList.remove('active');
    // Bg3.classList.remove('active');

    changeBG();
})

Bg3.addEventListener('click', () =>{
    removeBgSelector();
    Bg3.classList.toggle('active');

    whiteColorLightness = '10%';
    lightColorLightness = '0%';
    darkColorLightness = '95%';

    // Bg3.classList.add('active');
    // Bg2.classList.remove('active');
    // Bg1.classList.remove('active');

    changeBG();
})



