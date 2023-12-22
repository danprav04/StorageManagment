const api_path = 'api';

// Get Users
async function getUsers() {
    const url = `${api_path}/get_users`;
    const users = await async_get_request(url);
    return users
}

// Get Storage Places
async function getStoragePlaces() {
    const url = `${api_path}/get_storage_places`;
    const storagePlaces = await async_get_request(url);
    return storagePlaces
}

// Create Storage Place
async function createStoragePlace(name, description, image) {
    const url = `${api_path}/create_storage_place`;
    const postData = { name, description, image };

    const result = await async_post_request(url, postData);
    return result
}

// Create Storage Grid
async function createStorageGrid(name, description, rowCount, columnCount, image, storagePlaceId) {
    const url = `${api_path}/create_storage_grid`;
    const postData = { name, description, row_count: rowCount, column_count: columnCount, image, storage_place_id: storagePlaceId };

    const result = await async_post_request(url, postData);
    return result
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

    const result = await async_post_request(url, postData);
    return result
}

// Get Storage Grids
async function getStorageGrids() {
    const url = `${api_path}/get_storage_grids`;
    const storageGrids = await async_get_request(url);
    return storageGrids
}

// Get Storage Units
async function getStorageUnits() {
    const url = `${api_path}/get_storage_units`;
    const storageUnits = await async_get_request(url);
    return storageUnits
}
