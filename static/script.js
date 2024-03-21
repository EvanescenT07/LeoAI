document.getElementById('start').addEventListener('click', function() {
      fetch('/process_voice_input', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({ user_input: 'What is your name?' })
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
          document.getElementById('output').innerText = data.output;
          animateWaves();
      })
      .catch(error => {
          console.error('Error:', error);
          // Display error message to the user
          alert('An error occurred. Please try again later.');
      });
  });
  
  function animateWaves() {
      const waves = document.querySelectorAll('.wave');
      const animationDelayIncrement = 0.2; // Adjust this value if needed
      waves.forEach((wave, index) => {
          wave.style.animationDelay = `${index * animationDelayIncrement}s`;
      });
  }