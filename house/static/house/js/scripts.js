console.log("33333333")

$(document).ready(function() {
            $("#light_1").css("opacity", light_opp);
        });
function updateTemperature() {
      $.ajax({
        url: '/get_temperature/',
        type: 'POST',
        beforeSend: function(xhr, settings) {
          xhr.setRequestHeader("X-CSRFToken", csrfToken);
        },
        success: function(response) {
          $('#temperature-value').text(response.temperature + '°C');
          console.log("11111111")
          $('#is_heating').text(response.is_heating);
        },
        error: function(error) {
          console.log('Произошла ошибка:', error);
        }
      });
    }

setInterval(updateTemperature, 10000);


// Функция для обновления статуса освещения
function updateLightStatus() {
  let lightStateRoom2 = $('#light_state_room2').data('room2');
  let lightStateRoom3 = $('#light_state_room3').data('room3');
  let lightStateRoom4 = $('#light_state_room4').data('room4');
  let lightIndicator2 = $('#light_2');
  let lightIndicator3 = $('#light_3');
  let lightIndicator4 = $('#light_4');



  if (lightStateRoom2 === 'Off') {
    lightIndicator2.hide(); // Скрыть кружок
  } else if (lightStateRoom2 === 'On') {
    lightIndicator2.show(); // Показать кружок
  }

  if (lightStateRoom3 === 'Off') {
    lightIndicator3.hide(); // Скрыть кружок
  } else if (lightStateRoom3 === 'On') {
    lightIndicator3.show(); // Показать кружок
  }

  if (lightStateRoom4 === 'Off') {
    lightIndicator4.hide(); // Скрыть кружок
  } else if (lightStateRoom4 === 'On') {
    lightIndicator4.show(); // Показать кружок
  }
}

// // Вызов функции при загрузке страницы
$(document).ready(function() {
  updateLightStatus();
});

// Обновление статуса освещения при отправке формы
$('form').submit(function() {
  setTimeout(updateLightStatus, 100);
});