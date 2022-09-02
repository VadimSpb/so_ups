## Сбор данных по генерации и потреблению электроэнергии с сайта [Системного оператора Единой энергетической системы](https://www.so-ups.ru/)

Перед запуском не забудь установить библиотеки из файла [requirements.txt](https://github.com/VadimSpb/so_ups/blob/master/requirements.txt)

Точка запуска - файл [main.py](https://github.com/VadimSpb/so_ups/blob/master/main.py).

В итоге вы получаете три списка:

* **times** - список дат и времени
* **generated** - список генерации электроэнергии
* **spent** - список трат электроэнергии 

```time.sleep(1)``` вставлен, чтобы не ддосить сайт.

А дальше делайте с инфой что хотите - можно запихнуть в словарь (json),
 можно отправить в базу данных, можно вставлять в датафрейм.
Можно сделать налету преобразование списка ```str``` в список  ```datetime```.

Дальнейшие шаги - можно сбор инфы обернуть в функцию, результат - в объект 
или в драйвер для отправки в БД. Или склеивать в ```dataframe``` и джойнить для дальнейшей отрисовки и анализа.


Тут есть подстава - три списка. Они необязательно будут равной длинны. Это надо обработать.

Если вы хотите получить многопоточность - можно использовать [scrapy](https://scrapy.org/)

**Права*** - берите кто угодно, используйте для чего угодно.