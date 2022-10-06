Link herokuapp: https://tugas2pbphanin.herokuapp.com/todolist/login/

1. - Inline CSS adalah cara penulisan styling CSS yang dilakukan langsung dalam tag elemen yang bersangkutan. Hal ini membuat stylingnya spesifik pada satu elemen dan tidak dependen dengan styling lainnya.

- Internal CSS adalah cara penulisan CSS yang berada di file yang sama pada file HTML. Styling CSS tersebut unik untuk file HTML itu saja. Internal CSS ditulis menggunakan tag <style> .selector {styling properties} </style>.

- Eksternal CSS adalah cara penulisan CSS pada satu file yang terpisah dari HTML. Untuk menggunakan CSS tersebut pada file HTML gunakan tag <link rel="stylesheet" href="mystyle.css">. File yang dituliskan dalam href adalah nama file .css yang telah dibuat. Isi dari file CSS eksternal akan mengubah styling untuk semua file .html.

2. Beberapa tag HTML yang umum digunakan adalah :
"<head> : Head berisi metadata yang biasanya menyatakan judul dokumen, character set, styles, scripts, dan informasi meta lainnya
<body> : Body berisi data yang ingin ditampilkan di website
<input> : untuk menerima input dari user
<h1>, <h2>, <h3>, dll : Heading tag dari 1-6 (ukuran 1 adalah paling besar)
<div> : container (division)
<p> : untuk text paragraf (paragraph)
<form> : untuk membuat form" 

3. Terdapat 6 tipe selector CSS, yaitu:

- Tag : type selector untuk memilih elemen berdasarkan tag. (tag p, button, table, dll)
p {
    insert code here
}
- Class : memilih elemen berdasarkan nama class yang sudah diberikan (<p class="nama-class"></p>)
.nama-class {
    insert code here
}
- Atribut : memilih elemen berdasarkan attribut dari sebuah tag. Misalnya tag input memiliki beberapa tipe, salah satunya adalah text.
input[type=text] {
    insert code here
}
- ID : memilih elemen berdasarkan id (<p id="nama-id"></p>)
#nama-id {
    insert code here
}
- Pseudo : a. pseudo-class : menyatakan state element (click, hover, dll)
a:hover {
    insert code here
}
b. pseudo-element : untuk element semu di HTML , misal seperti elemen di dalam elemen

p span{
    insert code here
}
- Universal : selektor ini akan berlaku untuk semua atribut
* {
    insert code here
}

4. - Menggunakan CSS untuk mengkustomisasi masing-masing halaman, dengan referensi dari internet (link website dari tutor sebelumnya)
   - Membuat cards dan mengkustomisasinya sesuai design halaman (referensi dari internet)
   - Memastikan keempat halaman responsif
   - Melakukan push dan deploy ke github dan heroku

