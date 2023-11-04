window.addEventListener('load', function(){

    let selected = document.querySelector('.menu_selected')
    if(selected){
        second_list_parent = selected.closest('.menu__inner_item_list') // меню второго порядка
        if(second_list_parent){
            second_list_parent.classList.add('show')
        }else{
            console.log("меню второго порядка не обноружено")
        }
        first_list_parent = selected.closest('.menu__inner_list') // выпадающее меню первого порядка
        if(first_list_parent){
            first_list_parent.classList.add('show')
        }else{
            console.log(' выпадающее меню первого порядка не обнаружено')
        }
    }else{
        console.log("элемента с классом menu_selected на странице не найдено")
    }
})