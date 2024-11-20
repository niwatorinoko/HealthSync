function calculateBedtime() {
    const wakeUpTime = document.getElementById('wake-up-time').value;
    if (!wakeUpTime) {
      document.getElementById('calculator-result').innerText = "Please select a wake-up time.";
      return;
    }
    
    const wakeUpDate = new Date();
    const [hours, minutes] = wakeUpTime.split(':');
    wakeUpDate.setHours(hours);
    wakeUpDate.setMinutes(minutes);
  
    // Assuming 8 hours of sleep
    const sleepDuration = 8 * 60 * 60 * 1000; // 8 hours in milliseconds
    const bedtime = new Date(wakeUpDate.getTime() - sleepDuration);
    
    const bedtimeHours = bedtime.getHours().toString().padStart(2, '0');
    const bedtimeMinutes = bedtime.getMinutes().toString().padStart(2, '0');
    document.getElementById('calculator-result').innerText = `Your ideal bedtime is: ${bedtimeHours}:${bedtimeMinutes}`;
  }
  