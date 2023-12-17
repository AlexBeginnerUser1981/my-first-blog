To install Nginx on macOS, you will need to run the following command.
Again, you will need to have Homebrew installed for this command to work correctly.
1. brew install nginx
2. nginx #run nginx server
3. 127.0.0.1:8080 #it's work
4. nginx -s reload|reopen|stop|quit #перезагрузка/стоп/выход
5. sudo ln -s /usr/local/etc/nginx/sites-available/winproject /usr/local/etc/nginx/sites-enabled
6. nginx -t #configuration test