# 2-14lab
**2 лабораторная: ** При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля. Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит: «Пароль принят», иначе: «Пароль не принят».
Через API сайта https://haveibeenpwned.com/Passwords происходит дополнительная проверка введённого пользователем пароля на утечку (для безопасности пароли передаются и принимаются с помощью k-анонимности, а не напрямую)
Библиотека для работы с сервисом: https://github.com/duongntbk/passpwnedcheck?tab=readme-ov-file https://pypi.org/project/passpwnedcheck/ (её использование: 30-38 строчки кода)
Если пароль попал в утечку, то пользователю об этом сообщается со счетчиком

**10 лабораторная:** При создании отсортированного файла-алфавита en-ru_sorted.txt добавить пользователю возможность напрямую расширить его. С помощью API гугл-переводчика программа передаёт нужное слово/словосочетание, возвращает переведенную и оригинальную версию и передаёт их в текстовый файл. Возможность добавления новых слов неограничена и действует в реальном времени
Библиотека для работы с сервисом: https://github.com/ssut/py-googletrans?tab=readme-ov-file (её использование: 107-122 строчки кода)
примечания: без ошибок библиотека работает только с версией 3.1.0a0, требует питон 3.6+
