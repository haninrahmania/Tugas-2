1. Link menuju Heroku: 
2. CSRF (Cross Site Request Forgery) merupakan ancaman yang sering terjadi, oleh karena itu django menyediakan method untuk mencegahnya. {% csrf_token %} digunakan untuk mencegah serangan malicious dengan cara men-generate sebuah token dan memastikan requests yang kembali di cross-check dengan token ini saat sebuah page di generate. Jika token ini tidak termasuk dalam request yang datang, maka tidak di eksekusi.
   Jika tidak ada potongan code tersebut pada form, maka form tersebut tidak terlindungi dari CSRF.
3. Tanpa generator seperti {{ form.as_table }} kita tetap bisa membuat form secara manual, dengan cara menuliskan dalam <table> input type, name, placeholder, dan class.
   
