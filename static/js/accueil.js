// sidebar
const menuItems = document.querySelectorAll('.menu-item');

// discussions
const discNotification = document.getElementById('messages-notifications');
// const discNotification = document.querySelectorAll('#messages-notifications');
const discussion = document.querySelectorAll('.discussion');




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
        if(item.id != 'notifications'){
            document.querySelector('.notifications-popup').style.display  = "none";
        } else{
            document.querySelector('.notifications-popup').style.display  = "block";
            document.querySelector('#notifications .notifications-count').style.display = "none";
        }
    })
})


// ============ end SIDEBAR ===============


// =============== discussions =============

discNotification.addEventListener('click', () =>{
    discussion.forEach(item => {
        discNotification.querySelector('.notifications-count').style.display = "none";
        item.style.boxShadow = '0 0 1rem var(--color-primary)';
        setTimeout(() =>{
            item.style.boxShadow = 'none';
        }, 2000);
    })
})



// =============== end discussions ================
