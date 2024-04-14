![caubasephotos2](https://github.com/Uks130322/pereval/assets/101522861/2cef4890-8ebd-4f29-b3ac-bd86e15228b8)

На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами.

После преодоления очередного перевала, турист заполняет отчёт в формате PDF и отправляет его на электронную почту федерации. Экспертная группа ФСТР получает эту информацию, верифицирует, а затем вносит её в базу, которая ведётся в Google-таблице.

ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Пример JSON-а:
```JSON
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "что соединяет, текстовое поле",
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  "level": {"winter": "",
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   "images": [{"data": "<картинка1>", "title": "Седловина"}, {"data": "<картинка>", "title": "Подъём"}]
}
```
Результат метода: JSON

status — код HTTP, целое число:
500 — ошибка при выполнении операции;
400 — Bad Request (при нехватке полей);
200 — успех.
message — строка:
Причина ошибки (если она была);
Отправлено успешно;
Если отправка успешна, дополнительно возвращается id вставленной записи.
id — идентификатор, который был присвоен объекту при добавлении в базу данных.

Результат метода: JSON

status — код HTTP, целое число:
500 — ошибка при выполнении операции;
400 — Bad Request (при нехватке полей);
200 — успех.
message — строка:
Причина ошибки (если она была);
Отправлено успешно;
Если отправка успешна, дополнительно возвращается id вставленной записи.
id — идентификатор, который был присвоен объекту при добавлении в базу данных.
