const urlParams = new URLSearchParams(window.location.search);
const div_list = document.getElementById('list')

function append_section(div_list, title, description, image, id){
    var section = document.createElement('section')

    var title_cnt = document.createElement('h2')
    title_cnt.innerText = title

    var description_cnt = document.createElement('p')
    description_cnt.innerText = description

    var image_cnt = document.createElement('img')
    image_cnt.src = `static/pictures/${list_type}/${image}`
    image_cnt.alt = 'Picture of the displayed element.'

    section.appendChild(image_cnt)
    section.appendChild(title_cnt)
    section.appendChild(description_cnt)

    div_list.appendChild(section)

    section.addEventListener('click', (e) => {
        if(list_type == 'storage_places')
            location.href = `/storage_place?place=${id}`
        if(list_type == 'storage_grids')
            location.href = `/storage_grid?grid=${id}`
    })
}

function generateData(data) {
    for (var place of data){
        append_section(div_list, place['name'], place['description'], place['image'], place['id'])
        div_list.appendChild(document.createElement('hr'))
    }
}

if(list_type == 'storage_places')
    getStoragePlaces().then(data => {
        generateData(data)
    })

if(list_type == 'storage_grids' && urlParams.get('place'))
    getStorageGridsByPlaceId(urlParams.get('place')).then(data => {
        generateData(data)
    })

if(list_type == 'storage_units' && urlParams.get('grid'))
    getStorageUnitsByGridId(urlParams.get('grid')).then(data => {
        generateData(data)
    })
