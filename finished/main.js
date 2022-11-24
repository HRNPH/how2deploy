// requst get using axios
const api_route = 'http://127.0.0.1:8000/predict';

function predict() {
    input = document.getElementById('input_sentence');
    prediction_text = document.getElementById('prediction_text');
    sample_text = document.getElementById('sample_text');
    sentence = input.value;
    // Reset text and show loading
    input.value = '';
    sample_text.innerHTML = sentence;
    prediction_text.innerHTML = 'กำลังตรวจสอบ...';
    // predict
    axios.get(api_route, {
        // sentence to predict
        params: {
            text: sentence
        }
    }).then((response) => {
        prediction_text.innerHTML = response.data.sentiment;
    }).catch((error) => {
        console.log(error);
    });
}