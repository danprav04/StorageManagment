const api_path = 'api';

// Get Users
async function getUsers() {
    const url = `${api_path}/get_users`;
    return async_get_request(url)
}

// Get Storage Places
async function getStoragePlaces() {
    const url = `${api_path}/get_storage_places`;
    return async_get_request(url)
}

// Create Storage Place
async function createStoragePlace(name, description, image) {
    const url = `${api_path}/create_storage_place`;
    const postData = { name, description, image };

    return async_post_request(url, postData)
}

// Create Storage Grid
async function createStorageGrid(name, description, rowCount, columnCount, image, storagePlaceId) {
    const url = `${api_path}/create_storage_grid`;
    const postData = { name, description, row_count: rowCount, column_count: columnCount, image, storage_place_id: storagePlaceId };

    return async_post_request(url, postData)
}

// Create Storage Unit
async function createStorageUnit(name, description, image, storagePlaceId, storageGridId, storageGridRow, storageGridColumn) {
    const url = `${api_path}/create_storage_unit`;
    const postData = {
        name,
        description,
        image,
        storage_place_id: storagePlaceId,
        storage_grid_id: storageGridId,
        storage_grid_row: storageGridRow,
        storage_grid_column: storageGridColumn
    };

    return async_post_request(url, postData);
}

// Get Storage Grids
async function getStorageGrids() {
    const url = `${api_path}/get_storage_grids`;
    return async_get_request(url)
}

// Get Storage Units
async function getStorageUnits() {
    const url = `${api_path}/get_storage_units`;
    return async_get_request(url)
}
