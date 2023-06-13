document.write("<h1> hi</h1>");
document.write("<span> span </span>");

// this kind is {String} == object
console.log("mohamed shalan");

// this kind is {Number} == objectf
console.log(5000);

// this kind is {Array} == object
console.log([10, 15, 14]);
console.log(["mohamed", "ahmed"]);
console.log(["mohamed", "ahmed"]);
console.log(
  "welcome to %cJS %cfile",
  "color : blue; font-size:50px;",
  "color :red; font-size:25px;"
);

//  \Escape +  How ?
console.log("Mohamed Shalan will be a professional web 'developer'");
console.log(
  'Mohamed Shalan will be a %c\\$%c professional web %c"%cdeveloper %c" ',
  "font-size:40px; color:blue;",
  "font-size:12px; color:white;",
  "font-size:40px; color:blue;",
  "font-size:12px; color:white;",
  "font-size:40px; color:blue;"
);

//this kind is a Reall {object}
console.log({ name: "mo", age: 18, country: "eg" });

// line containue
console.log("Mohamed Shalan\nwill be a \nprofessional web developer");
console.log("Mohamed Shalan\t\twill be a \t\tprofessional web developer");
console.log("Mohamed Shalan \
will be a \
professional web developer");

//this kind is  a {boolean}
console.log(true);
console.log(false);

//this kind is  a {undefined}
console.log(undefined);

//this kind is  a {null}
console.log(null);

//this is wayes to Variables
//this var can use it any where in system and any number
var user1 = "mohamed",
  numb = 200;
//or   var user1 = "mohamed" ;
//var numb = 200 ;

console.log(user1);
console.log(user1);
console.log(user1);

console.log(++numb);
console.log(++numb);
console.log(++numb);

console.log(hallo);

let a = "we love";
let b = "js";
document.write(a + " " + b);

console.log(
  "%cElzero %cWeb %cSchool",
  "font-size:40px; color:red;",
  "font-size:40px; color:green;",
  "font-size:40px; color:white; background:blue;"
);

// this is a group in console
console.group("Group 1");
console.log("massage 1");
console.log("massage 2");

console.group("Chiled group");
console.log("massage 1");
console.log("massage 2");

console.group("Grand Chiled group");
console.log("massage 1");
console.log("massage 2");

console.groupEnd();
console.groupEnd();

console.groupEnd("Group 1");

console.group("Group 2");
console.log("massage 1");
console.log("massage 2");
console.groupEnd();

let title_card = "Hallo Elzero",
  disc_card = "Elzero web school",
  date_card = "25/10";

// `` هى طريقه تسهيل الكتابه عن كريق الكتابه داخلها
// `` الى بيتكتب جواها بيطلع ذى ما هوا
// a b and c = string

// old way
//console.log(a + " " + b + " ");
// new way
//console.log(` ${a}+ ${b}+ ${c}`);

let card = `
    <div class ='card'>
          <h1>${title_card}</h1>
          <p>${disc_card}</p>
          <span>${date_card}</span>
    </div>
    `;

let card2 = `
    <div class=""mo>
      <div>${title_card}</div>
      <p>${disc_card}</p>
      <div>${date_card}</div>
    </div>
`;

let card3 = `
  <div class="card">
  <h2>${title_card}<h1/>
  </div>
`;
document.write(card.repeat(4));
// let let1 = "we love";
// let let2 = "js";
// let let3 = "and ";
// let let4 = "programing ";

// console.log (` ${let1} \n ${let2} ${let3} ${let4}`);
// document.write (` ${let1} \n ${let2} ${let3} ${let4}`);

let num1 = 10;
let num2 = 20;

console.log(` ${100 * num1 + num2}`);
console.log(` ${num1} \n ${num2}`);
console.log(num1 + "\n" + num2);
elzero = { name: "mohamed", age: 19 };
console.log(elzero.innerHTML); // object
console.log(typeof elzero); // object

console.log(100);
console.log(+"100");
console.log(+"-100");
console.log(+"15.54");
console.log(Number("100"));
let z = "10";
let x = 10;
let u = "ahmad";

console.log(-"100");
console.log(-"-100");
console.log(+"100");
console.log(-true);
console.log(+z - +x);
console.log(`${z - x} `);
console.log(`${z - u} `);

let k = 20;
k = k + 40;
console.log(k);
console.log(+k);

k = 20;
k += 40; // this is prosies applay to ( / * - %)
console.log(k);
console.log(++k + ++k);
console.log(k);
console.log(+k++);
console.log(k);

// e is naumber of zeroes
console.log(1.7e308);
console.log(1e6);
console.log(1_000_000);
console.log(Number.MAX_SAFE_INTEGER);
console.log(Number.MIN_SAFE_INTEGER);
console.log(Number.MAX_VALUE);
console.log(Number.MIN_VALUE);
console.log(Number.MAX_VALUE * Number.MIN_VALUE);
console.log((12312512135351513 * 2) / 4);
console.log(12312512135351513 / 2);
console.log(5726718050568503295 + 1);
console.log(2 ** 4);
//                           (

// like %0.2f in c programing
console.log(parseInt((1000.05555).toFixed(0)));

// to bake string from number
console.log((100).toString());
// or console.log(100..tostring());7

//to backe number from string but this better then + and Number()
//this is try to search for number in his order
console.log(parseInt("100"));
// search from number
console.log(parseInt("100 mohamed"));
// not all way
console.log(parseInt("mohamed 100 mohamed"));

// no search
console.log(+"100");
console.log(Number("100"));

//                         )

// is
// interger عدد صحيح
console.log(Number.isInteger("100"));
console.log(Number.isInteger(100.557));
console.log(Number.isInteger(100));

console.log(Number.isNaN("osame"));

let app = 100.654856;

console.log(app.toFixed(2));

console.log(parseFloat(app.toFixed(2)));

console.log(Math.floor(-5.5));
console.log(Math.trunc(-5.5));

console.log(Math.floor(5.5));
console.log(Math.trunc(5.5));

// math
///////////
// flot number  {
// round {this normal proces } 5.95 result (6) , 5.2 result (5)
// ceil   5.95 result (6) , 5.2 result (6)
// floor  5.95 result (5) , 5.2 result (5)    1
// trunc  5.95 result (5) , 5.2 result (5)    2
// 1 dont equal 2
// for exaple     floor -5.5 > 6     >> min uumber
//                trunc -5.5 > 5     >> remove number after .
//              }
///////////
// for get a target number with math {
// math.max (100, 200, 59, -145, 5, 55)
// math.min (100, 200, 59, -145, 5, 55)
///////////

// challange
///////////  {
let a1 = 1_00;
let b1 = 2_00.5;
let c1 = 1e2;
let d1 = 2.4;

console.log(Math.min(a1, b1, c1, d1));

console.log(Math.trunc(d1) * 100 + a1 * 8);
console.log(`${d1 + 0.1}` * 80 + a1 * 8);

console.log(parseInt(d1.toFixed()));
console.log(Math.round(d1));
console.log(Math.floor(d1));
console.log(Math.trunc(d1));

console.log(((b1 / 10) * 3 + d1 * 2.718).toFixed(2));
console.log(Math.ceil((b1 / 10) * 3 + d1 * 2.718));
///////////  }

///////////  {
let thename = "  m0hamed  ";
//All
console.log(thename[3]);
// for wordes
console.log(thename.charAt[3]);
//number of eorder or number in value
console.log(thename.length);
//backe value untile spaces
console.log(thename.trim());

console.log(thename.toUpperCase());
console.log(thename.toLowerCase());
///////////  }

console.log(thename.trim().toUpperCase()[0]);
let j = 0;
for (j; j < 10; ++j) {
  console.log(j);
  console.log(j);
}
