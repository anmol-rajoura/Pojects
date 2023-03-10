const timeE = document.getElementById('time');
const dateE = document.getElementById('date');
const currentWeatherItem= document.getElementById('current-weather-item');
const timezone = document.getElementById('time-zone');
const country= document.getElementById('country');
const weatherForecast = document.getElementById('weather-forecast');
const currentTemp = document.getElementById('current-temp');

const days=['Sunday', 'Monday','Tuesday','Wednesday','Thursday', 'Friday', 'Saturday'];
const months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sept','Oct','Nov','Dec'];

const API_KEY = 'b66466d9738c07ecbb2721accbf01ef0';

setInterval(() =>{
    const time = new Date();
    const month= time.getMonth();
    const date = time.getDate();
    const day = time.getDay();
    const hours = time.getHours();
    const hoursIn12HrFormat = hours >=13? hours %12: hours
    const minutes = time.getMinutes();
    const ampm = hours>=12? 'PM' :'AM'

    timeE.innerHTML = (hoursIn12HrFormat <10? '0'+hoursIn12HrFormat:hoursIn12HrFormat) + ':' + (minutes<10? '0'+ minutes: minutes) + ' ' + `<span id="am-pm"> ${ampm}</span>`
    
    dateE.innerHTML = days[day] + ',' +date+ ' '+ months[month];
},1000);

getWeatherData();
function getWeatherData(){
    navigator.geolocation.getCurrentPosition((success)=>{
        
        let{latitude, longitude} = success.coords;

        fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${latitude}&lon=${longitude}&exclude=hourly,mintuly&units=metric&appid=${API_KEY}`).then(res => res.json()).then(data => {
            console.log(data)
            showWeatherData(data);
        })
    })
}

function showWeatherData(data){
    let{humidity, pressure, sunrise, sunset, wind_speed}= data.current;

    timezone.innerHTML =data.timezone;
    country.innerHTML=data.lat + 'N ' + data.lon + 'E'
    currentWeatherItem.innerHTML = `<div class="weather-item">
    <div>Humidity</div>
    <div>${humidity}%</div>
  </div>
  <div class="weather-item">
    <div>Pressure</div>
    <div>${pressure}</div>
  </div>
  <div class="weather-item">
    <div>Wind Speed</div>
    <div>${wind_speed}</div>
  </div>
  <div class="weather-item">
    <div>Sunrise</div>
    <div>${window.moment(sunrise*1000).format('HH:mm a')}</div>
  </div>
  <div class="weather-item">
    <div>Sunset</div>
    <div>${window.moment(sunset*1000).format('HH:mm a')}</div>
  </div>`;
  
  let otherDayForcast=''
  data.daily.forEach((day,idx)=>{
    if(idx==0){
      currentTemp.innerHTML = `
      <img src="http://openweathermap.org/img/wn/${day.weather[0].icon}@4x.png" alt="weather-icon" class="w-icon">
      <div class="other">
          <div class="day">${window.moment(day.dt*1000).format('dddd')}</div>
          <div class="temp">Night - ${day.temp.night}&#176;C</div>
          <div class="temp">Day - ${day.temp.day}&#176;C</div>
      </div>`
    }
    else{
        otherDayForcast += `<div class="weather-forecast-item">
        <div class="day">${window.moment(day.dt*1000).format('ddd')}</div>
        <img src="http://openweathermap.org/img/wn/${day.weather[0].icon}@2x.png" alt="weather-icon" class="w-icon">
        <div class="temp">Night - ${day.temp.night}&#176;C</div>
        <div class="temp">Day - ${day.temp.day}&#176;C</div>
</div>`
    }
  })
  
  weatherForecast.innerHTML = otherDayForcast;
}