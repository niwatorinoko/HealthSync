function showSleepTips() {
    const hours = document.getElementById('sleep-hours').value;
    const quality = document.getElementById('sleep-quality').value;
    const tipsContainer = document.getElementById('sleep-tips');
    let message = '';
  
    if (!hours || !quality) {
      message = 'Please fill in all fields.';
    } else if (hours < 7 || quality === 'poor') {
      message = `
        <p><strong>Tips for better sleep:</strong></p>
        <ul>
          <li>Set a consistent bedtime and wake-up time.</li>
          <li>Reduce screen time at least 1 hour before bed.</li>
          <li>Practice relaxation techniques, like deep breathing.</li>
        </ul>
      `;
    } else {
      message = `<p>Your sleep habits seem great! Keep maintaining them.</p>`;
    }
  
    tipsContainer.innerHTML = message;
  }
  