async function async_post_request(url, postData){
    const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(postData)
      };
      
      try {
        const response = await fetch(url, options);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error during POST request:', error);
    }
}

async function async_get_request(url){
    const options = {
        method: 'GET',
        headers: {
        }
    };
      
    try {
        const response = await fetch(url, options);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error during GET request:', error);
    }
}
