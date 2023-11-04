window.addEventListener('load', function(){
    let elements = document.querySelectorAll(".menu__select"); // элементы меню с выпадающем списком
    let ulLists = document.querySelectorAll('.menu__inner_list') // выпадающие списки первого порядка
    let menu_item = document.querySelectorAll('.menu__item') // все элементы меню первого порядка
    let inner_list = document.querySelectorAll('.menu__inner_item_list') // выпадающие списки второго порядка
    let inner_link = document.querySelectorAll('.js_menu__inner_item') // элемент второго порядка с выпадающем списком

// при наведение на элемент меню который является ссылкой, убирать все выпадающие списки
    menu_item.forEach(function(element){
    element.addEventListener("mouseover", function(e) {
            ulLists.forEach(function(e){
                e.classList.remove('show')
            })
            inner_list.forEach(function(e){
                e.classList.remove('show')
            })
         })
    });



// при наведение на элемент которы является выпадающим списком
    elements.forEach(function(element) {
        element.addEventListener("mouseover", function(e) {
            // добавляем выпадающему списку класс show
            e.preventDefault()
            let ulList = this.nextElementSibling;
            ulList.classList.add('show')
        })
    });

    inner_link.forEach(function(e){
        e.addEventListener('click', function(element){
            element.preventDefault()
            inner_list.forEach(function(e){
                e.classList.remove('show')
            })
        })
    })

// при клике на элемент второго порядка открываем выпадающий список
    inner_link.forEach(function(e){
        e.addEventListener('click', function(elem){
            elem.preventDefault()
            let ulList = this.nextElementSibling;
            console.log(ulList.classList)
            if (ulList.classList.contains('show')){
                ulList.classList.remove('show')
            }else{
                ulList.classList.add('show')
                console.log(ulList.classList)

            }
        })
    });




})