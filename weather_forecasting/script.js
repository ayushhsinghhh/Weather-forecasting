function getWeather() {
    const city = document.getElementById("cityInput").value;
    const apiKey = '15811823f2b648f8be7133621242304';
    const apiUrl = `http://api.weatherapi.com/v1/current.json?key=${apiKey}&q=${city}`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const weatherResult = document.getElementById("weatherResult");
            weatherResult.innerHTML = `
                <h2>${data.location.name}, ${data.location.country}</h2>
                <p>Weather: ${data.current.condition.text}</p>
                <p>Temperature: ${data.current.temp_c}°C</p>
                <p>Humidity: ${data.current.humidity}%</p>
            `;
        })
        .catch(error => {
            console.error("Error fetching weather data:", error);
            const weatherResult = document.getElementById("weatherResult");
            weatherResult.innerHTML = "<p>Failed to fetch weather data. Please try again later.</p>";
        });
}
