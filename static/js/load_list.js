function append_section(div_list, title, description, image){
    var section = document.createElement('section')

    var title_cnt = document.createElement('h2')
    title_cnt.innerText = title

    var description_cnt = document.createElement('p')
    description_cnt.innerText = description

    var image_cnt = document.createElement('img')
    image_cnt.src = `static/pictures/storage_places/${image}`
    image_cnt.alt = 'Picture of the displayed element.'

    section.appendChild(image_cnt)
    section.appendChild(title_cnt)
    section.appendChild(description_cnt)

    div_list.appendChild(section)
}

getStoragePlaces().then(data => {
    const div_list = document.getElementById('list')

    for (var place of data){
        append_section(div_list, place['name'], place['description'], place['image'])
        div_list.appendChild(document.createElement('hr'))
    }
})
