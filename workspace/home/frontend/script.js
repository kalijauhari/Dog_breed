// script.js (Frontend JavaScript)
async function classifyImage() {
  const fileInput = document.getElementById('imageInput');
  const file = fileInput.files[0];

  const formData = new FormData();
  formData.append('image', file);

  try {
      const response = await fetch('/classify', {
          method: 'POST',
          body: formData
      });
      const data = await response.json();
      displayResults(data.classification);
  } catch (error) {
      console.error('Error:', error);
  }
}

function displayResults(classification) {
  const resultsDiv = document.getElementById('result');
  resultsDiv.innerHTML = `Classification: ${classification}`;
}
