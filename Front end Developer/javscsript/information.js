//window.alert("mohamed");
// document.write("<h1>hallo<h1/>");
console.table(["osama ", "mohamed ", "%cahmad"], "color:red;");
console.log(
  "i will be a %cprofessional %cfull-stack developer",
  "font-size:20px;color:red;text-align:center;",
  "color:white;font-size:20px;text-align:center;"
);
console.log(`hi`);

///-------------_type of data_---------------- ///
console.log(typeof "mohamed shalan"); //string
console.log(typeof 5000); // number
console.log(typeof -8554); // number
console.log(typeof [10, 15, 17, 15, 88]); // Array = object
console.log(typeof ["mohamed", "as", "saiead", "shalan"]); // Array = object
console.log(typeof { name: "mohamed", age: 19, country: "Egypt" }); // object
console.log(typeof true); // (logic , yas)
console.log(typeof false); // (not logic , no)
console.log(typeof undefined);
console.log(typeof null);
console.log(typeof null);

var user52365 = {
  fname: "Mohamed",
  mname: "Elsaiead",
  lname: "Shalan",
  age: 19,
  gender: "Male",
};
var user = " mohamed";
// user_name.innerHTML = user;
console.log(user52365.fname);
// ---------------_name of variable_---------------\\
// identifiers >> this rules of name varuable
// (1user,us er, user@ , @user, us@er) No
// no accept spoical CARACTER except $
// (_u_s_er_ , use1r, ( User , user ) , useR ) Yas
// some way to set a name to variable this->>
// mohamedElsaieadShalan _or_ mohamed_elsaiead_Shalan

// -------------- type of declare varuable -------------- \\
/*
  var 
  -- redeclar(Yas) 
  -- Access before Declare (undefined)
  -- Variable scope drama [added to window ]
  
  let  
  -- redeclar(no >>Error) 
  -- Access before Declare (Error )
  -- Variable scope drama [don't added to window ]
  
  const
  -- redeclar(no >>Error) 
  -- Access before Declare (Error)
  -- Variable scope drama [added to window ]
*/
/*
  some string syntax and Character Escape 
*/
///-------------------------- way to Write '' ------///////////
//console.log('Mohamed "Shalan"');
//console.log(" Mohamed \"Shalan\" "); <_>
// ----------output ----->> Mohamed "Shalan"
//console.log("Mohamed 'Shalan'");
//console.log('Mohamed \'Shalan\'');

/*
console.log(  |  cnosole.log("mohamed\nShalan") |  //tis is the same output
  "mohamed    |                                 |
  shalan"     |                                 |
  );          |                                 |
*/
console.log(`hi my name is ' Mohamed '\rShalan`);
///------------------------- concatenation --------//////////////////
// let a = "I love ";
// let b = "JS";

let userName = "Mohamed";
// document.write(a + b);
///------------------------- Template Literals Template String -----------////
// console.log(`
// ----hi my name is
//   ${userName}
// this is write by \`\`
// ${a}it`);
let cardHTML = `
  <div>
    <div class="title"  style="font-weight:700;">
      ${userName}
    </div>
    <div class="discription" style="color:red;">
      Hi my name is ${userName} , Now i learn JS
    </div>
  </div>`;
document.write(cardHTML);
///------------------------- small challange ------------------///
let webTitle = "Elzero",
  decriptionTitle = "Elzero Web School",
  dataCreate = "25/10";
let card = `
      <div>
          <h3 style='color:red;'>Hallo ${webTitle}</h3>
          <p>${decriptionTitle}</p>
          <span>${dataCreate}</span>
        </div>
`;
// document.write(card.repeat(4));
///------------------------ arithmetic operation --------------///

console.log(10 + 20); //output 30
console.log(10 + "mohamed"); //output 10mohamed
console.log(10 - 20); //output -10
console.log(10 - "mohamed"); //output NaN
console.log(2 ** 4); //output 16
console.log(10 / 2); //output 5
console.log(11 / 2); //output 5.5
console.log(11 % 2); //output 1
console.log(10 * 20); //output 200 in page
console.log(26 % 3); //output 2
num = 1;
console.log(++num); // output 2 then value is 2
num = 1;
console.log(num++); // output 1 then value is 2
//++++++++++++++++++++++++++++ Plus return number
console.log(+100); //return Number 100
console.log(+"100"); //return Number 100
console.log(+"-100"); //return Number -100
console.log(+"15.5"); //return Number 15.5
console.log(+"mohamed"); //return Number NaN
console.log(+0xff); //return Number 256
console.log(+null); //return Number 0
console.log(+false); //return Number 0
console.log(+true); //return Number 1
//---- ---- ---- ---- ---- ---- ----negation return number>then>converse to negation
console.log(-"100"); //return Number -100
console.log(-"-100"); //return Number 100
console.log(-"moahmed"); //return NaN
console.log(-null); //return Number -0
console.log(-false); //return Number -0
console.log(-true); //return Number -1
//---- ---- ---- ---- ----- ----
// (a = "10"), (b = 20), (c = true);

console.log(20 + "10"); // output 2010
// console.log(b + c /*1*/); // output 21
// console.log(b + c); // output 21
// console.log(a + b + c); // output 1020true التحويل بالاكراه
// to solve this
// console.log(+a + b + c);

// b += 5; // 25
// b = 25
// console.log(b);

// b -= 10; // 15
// b = 15
// console.log(b);
//------------------ chalenge 1 -------//
// a = 10;
// b = "20";
// c = 80;
// console.log(++a + +b++ + +c++ - +a++); // output 11+20+80-11= 100
// //++a //pre output 11 value 11
// //+   //add
// //+b++//+ returm number b++ output 20 value 21
// //+c++//+ returm number c++ output 80 value 81
// //-   //
// //+a++// return a
// console.log(a); //12
// console.log(b); //21
// console.log(c); //81

// console.log(++a /*13*/ + -b /*-21*/ + +c++ /*81*/ - -a++ /*-13*/ + +a /*14*/);
// // 13-21+81+13+14 = 100
// // ++a >> 13
// // -b  >> -21 >> 21
// //+c++ >> 81 >> 82
// //-a++ >> -13
// // +a  >> 14 >> 14
// console.log(--c + +b + --a * +b++ - +b * a + --a - +true);
// // 81 +21 + (13 * 21) - (22 * 13) + 12 + 1 = 100
// // --c >> 82 >> 81
// // +b  >> 21 >> 21
// // --a >> 13 >> 13
// // +b++>> 21 >> 22
// // +b  >> 22 >> 22
// //  a  >> 13 >> 13
// // --a >> 12 >> 12
// // true  >> 1 >> 1
// let d = "-100";
// let e = "20";
// let f = 30;
// let g = true;
// q = 20;
// console.log(-d * +e); // 2000
// console.log(-d + +e * 2 + f + +g * 3); // 173
// ------------------------------_Number_-----------------------//
// ------------------------basic ------------
console.log(Number(1000000));
console.log(Number(1_000_000));
console.log(Number(1e6));
console.log(Number(1000_000.0));
console.log(Number.MAX_VALUE);
console.log((Number.MAX_VALUE)+2) ;
console.log(Number.MAX_SAFE_INTEGER);

let r = 20,
  t = 10;
console.log(t / 0); // infinity

console.log((100).toString()); // return a number as string
console.log((100.5).toString()); // return a number as string
console.log((100.5467682).toFixed(2)); // return 100.55
console.log(parseInt(1000.5522)); /// return a integar number if this is a float
console.log(parseInt(1000)); ///      return a integar number if this is a float
console.log(parseInt("1000 mohamed")); /// teturn 1000
console.log(parseFloat("10.4550")); // return a float number
console.log(parseFloat("10.4550 Mohamed")); // return a float number

console.log(Number.isInteger(10000)); // True
console.log(Number.isInteger(100000.5555)); // False
console.log(Number.isNaN(100000.5555)); // false
console.log(Number.isNaN(100000.5555 / "moahmed")); // True
console.log(parseFloat("10.4550 Mohamed")); // return a float number
//-----------------------------_ Math Objoct _----------------//
console.log(Math.round(99.6)); // this whill be 100 ^
console.log(Math.round(99.1)); // this whill be 99
console.log(Math.floor(99.7)); // this whill be 99
console.log(Math.ceil(99.1)); // this whill be 100 ^
console.log(Math.trunc(99.9)); // this not up or down but this is remove a float part
console.log(Math.min(10, 20, 50, 400, 5056, -10)); // -10
console.log(Math.min(10, 20, 50, 400, 5056, -10)); // 5056
console.log(Math.pow(2, 4)); // this is the same 2 ** 4
//-------------------------- _Number Chalenge_--------------
let a = 1_00,
  b = 2_00.5,
  c = 1e2,
  d = 2.4;
// Find Smallest Number in All Variables And Return. Integer
console.log(Math.trunc(Math.min(a, b, c, d)));
// Use Variable a + d One Time To Get The Needed Output
console.log((Math.trunc(b) * a) / 2); // 10000
// Get Integer "2" From d Variable With 4. Methods
console.log(Math.round(d));
console.log(Math.floor(d));
console.log(Math.trunc(d));  
console.log(Number(d.toFixed(0)));
// Use Variables b + d To Get This Values
console.log((Math.trunc(b) / 3).toFixed(2)); // 66.67 => String
console.log((b / (d * 1.253)).toFixed(2)); // 66.67 => String
console.log(Math.ceil((Math.trunc(b) / 3).toFixed(2))); // 67 => Number
console.log(Math.ceil((b / (d * 1.253)).toFixed(2))); // 67 => Number
//-------------------------_string Methods_--------------
let theName = " M1ohamed";

console.log(theName);
console.log(theName[9]);
console.log(theName.charAt(9));
//-----------------------------------
// if this index not found output shoud be
/*undefind*/ console.log(theName[9]);
/*        */ console.log(theName.charAt(9));
//-----------------------------------
console.log(theName.length);
// return number of charactrer 8
// but index 8 is not here becuse Js is 0 Base index number , so the last index number is 7
//-----------------------------------
theName = "     mohamed     ";
console.log(theName.trim()); // trim is remove spaces // output is mohamed
console.log(theName.trim().charAt(2).toUpperCase()); // to return H
//------------------------_string Method_-----------------
let q = "Mohamed Elsaiead Shalan Elsaiead Shalan";
//-------this to search about character------> >
/*--*/ console.log(q.indexOf("Elsaiead")); // 8 // this return position index
/*--*/ console.log(q.lastIndexOf("S")); // 33 // search on last
/*--*/ console.log(q.includes("Elsaiead")); // True
/*--*/ console.log(q.includes("Elsaiead")); // True
/*--*/ console.log(q.includes("Elsaead")); // False
// include return true or false , and it applay start position
/*--*/ console.log(q.startsWith("M")); //true
// it can applay start position , this use length
/*--*/ console.log(q.startsWith("E", 8)); //true
/*--*/ console.log(q.startsWith("E", q.indexOf("Elsaiead") /*8*/));
//true
/*--*/ console.log(q.startsWith("M", 2)); //false
/*--*/ console.log(q.endsWith("n")); //true
//
//----
/*--*/ console.log(q.slice(q.lastIndexOf("Elsaiead"))); // cut a part ,if have no end then a defultt is 0
/*--*/ console.log(q.slice(5, 8)); // cut a part
/*--*/ console.log(q.slice(-5, -3)); // cut a part
//----
/*--*/ console.log(q.repeat(5)); // this is repeat varuable 5 items
//----
/*--*/ console.log(q.split(""));
// output//----['M', 'o', 'h', 'a', 'm', 'e', 'd', ' ', 'E', 'l', 's', 'a', 'i', 'e', 'a', 'd', ' ', 'S', 'h', 'a', 'l', 'a', 'n']
/*--*/ console.log(q.split(" "));
// output//----['Mohamed', 'Elsaiead', 'Shalan','Elsaiead', 'Shalan']
/*--*/ console.log(q.split(" ", 2));
// output//----['Mohamed', 'Elsaiead']
/*--*/ console.log(q.split(" Elsaiead"));
// output//----['Mohamed', 'Shalan']
/*--*/ console.log(q.length);
// counts a number of character varuable
//----
/*--*/ console.log(q.substring(0, 7)); // Mohamed
// this cut only this part , defult end is last caharacrter in varuable
/*--*/ console.log(q.substring(7, 0)); // Mohamed
// if end is bieger than start > > then nethode wiil reverse number to make start is biger
/*--*/ console.log(q.substring(-8, 7)); // == 0 , 7 // Mohamed
// if start is nigative > > this make start 0
/*--*/ console.log(
  q.substring(q.length - q.split(" ")[q.split(" ").length - 1].length)
);
// this is cut the last name is Shalan
//---
/*--*/ console.log(q.substr(0, 7)); // Mohamed
// this start is normal and start from 0 ,but not include end , this include length
/*--*/ console.log(q.substr(-6, 2)); // Sh // it lengyh to from start
/*--*/ console.log(q.substr(-6)); // Shala-n
// -----------------------Sring Challenge--------//
let w = "Elzero Web School";
/*--*/ console.log(w.charAt(2).toUpperCase() + w.slice(3, 6)); // Zero
/*--*/ console.log(w.slice(2, 6).toLocaleUpperCase()); // ZERO
/*--*/ console.log(w.substr(-4, 1).toUpperCase().repeat(8)); // HHHHHHHH
/*--*/ console.log(w.split(" ")[0]); //[Elzero]
/*--*/ console.log(w.substr(0, 7) + w.substr(-6)); // Elzero School
/*--*/ console.log(
  w.charAt(0).toLowerCase() +
    w.substr(1, w.length - 2).toUpperCase() +
    w.charAt(w.length - 1).toLowerCase()
); // eLZERO WEB SCHOOl
// --------------------- Comparison Operators --------//
/*--*/ console.log(10 == "10"); // true
/*--*/ console.log(10 != "10"); // false
/*--*/ console.log(-10 == "-10"); // true
// becouse == Compare value only , ( not compare between type )
/*--*/ console.log(-100 === "-100"); // false
/*--*/ console.log(-100 === -100); // true
/*--*/ console.log(-100 !== -100); // false
// becouse === Compare value and and type (===) << populeer
/*--*/ console.log(11 > "10"); // true
/*--*/ console.log(10 >= 10); // true
/*--*/ console.log(10 < 10); // false
/*--*/ console.log(10 <= 10); // true
//------------------- logical operators------ //
// ! ont
// && and
// || or

/*--*/ console.log(true); // ture
/*--*/ console.log(!true); // false
/*--*/ console.log(!(10 == "10") /*true*/); //false

/*--*/ console.log(100 == 100 && 10 > 8); //true
/*--*/ console.log(100 == 100 && 10 <= 8); // false

/*--*/ console.log(10 == 10 || 10 < 8 || 10 == 50); // true
/*--*/
//----- ----- ---- ----- --- elzero تكليفات

let c3 = 10;
let a1 = 20;
let b2 = 30;

console.log((a1 < b2 && a1 > c3) || a1 < b2); // true
console.log(a1 < b2 || a1 > c3); // true
console.log(!(a1 > b2) && !(a1 > b2) && !(a1 < c3) && !(a1 < c3)); // true

// -------------__if condetion __----------

var price = 100;
var genralDiscountAmount = 30;
var discount = false;
var country = "syria",
  discoutsyria = 60;
var discountEgypt = 50;

if (discount === true) {
  price -= genralDiscountAmount;
} else if (country == "Egypt") {
  price -= discountEgypt;
  console.log("The disco-unt is end in all countres else Egypt this is 70");
} else if (country == "syria") {
  price -= discoutsyria;
  console.log(
    "The discount is end in all countres else syria this is (price - 60)"
  );
} else {
  price -= 10;
}
console.log("-------------------------------");
let mohamed1 = {
  firstName: "mohamed",
  age: 19,
  gender: "male",
};
console.log(mohamed1.firstName);
//--------------conditional ternary operat--------//
let theName1 = "mohamed";
let gender = "male";

var price = 100;
var genralDiscountAmount = 30;
var discount = false;
var country = "syria",
  discoutsyria = 60;
var discountEgypt = 50;
(country = "syria"), (discoutsyria = 60);

let discountamoutn =
  country === "Egypt"
    ? (price -= discountEgypt)
    : country === "syria"
    ? (price -= discoutsyria)
    : (price -= genralDiscountAmount);

let genderOut = gender === "male" ? " Mr" : " Mrs";

let lastOutputDiscription = `<p style='font-size:16px;font-style:italic;color:red;'>
Hallo${genderOut}: ${
  theName1.charAt(0, 1).toUpperCase() + theName1.substring(1, theName1.length)
} your discount is ${discountamoutn}</p>`;

discountCard = `${lastOutputDiscription}`;
// document.write(discountCard);

// stert in lesson #36

//---------Nullish Coalescing Operator And Logical Or-------//

var falsePrice = 100;
console.log(`here we use a || to replac a not logic value`);
console.log(`-----price is ${falsePrice || 200}`);
var falsePrice = null;
console.log(`-----price is ${falsePrice || 200} the orignal value is null `);
var falsePrice = 0;
console.log(
  `-----price is ${
    falsePrice === 0 ? "free" : falsePrice
  } the orignal value is 0 `
);
var falsePrice = false;
console.log(`-----price is ${falsePrice || 200} the orignal value is false `);
var falsePrice = "";
console.log(`-----price is ${falsePrice || 200} the orignal value is '' `);

var falsePrice = 100;
console.log(`here we use a ?? to replac some not logic value`);
console.log(`-----price is ${falsePrice ?? 200}`);
var falsePrice = null;
console.log(`-----price is ${falsePrice ?? 200} the orignal value is null `);
var falsePrice = 0;
console.log(`-----price is ${falsePrice ?? 200} the orignal value is 0 `);
var falsePrice = false;
console.log(`-----price is ${falsePrice ?? 200} the orignal value is false `);
var falsePrice = "";
console.log(`-----price is ${falsePrice ?? 200} the orignal value is '' `);
//------------------------ if condition challeng---------//
let ab = 10;

// if (ab < 10) {
//   console.log(10);
// } else if (ab >= 10 && ab <= 40) {
//   console.log("10 To 40");
// } else if (ab > 40) {
//   console.log("> 40");
// } else {
//   console.log("Unknown");
// }
let abReturn =
    ab < 10
    ? 10
    : ab >= 10 && ab <= 40
    ? "10 To 40"
    : ab > 40
    ? "> 40"
    : "Unknown";
console.log(abReturn);

// Write With Ternary If Syntax

let st = "Elzero Web School";
console.log((st.length * 2).toString());
if ((st.length * 2).toString() === "34") {
  console.log("Good");
}
// //.W Poition May Change
if (st.substring(st.indexOf("W"), st.indexOf("W") + 1) === "W") {
  console.log("Good");
}
if (typeof st != "string") {
  console.log("Good");
}
if ((typeof st== typeof st ? "number" : "number") === "number") {
  console.log("Good");
}
if (st.split(" ")[0] + st.split(" ")[0] === "ElzeroElzero") {
  console.log("Good");
}
// ----------------------- Switch statment -----------//
let day = 5;
switch (day) {
  case 0:
    console.log("Saturday");
    break;
  case 1:
    console.log("Sunday");
    break;
  case 2:
    consol.log("Monday");
    break;
  case 3:
    console.log("Tuesdaay");
    break;
  case 4:
    consol.log("wednesday");
    break;
  case 5:
    console.log("Thurday");
    break;
  case 7: // we can use a multiple cases
  case 6:
    console.log("Friday");
    break;
  default:
    console.log("Unknown Day");
    break;
} 
//-------------- switch statment challenge--------//
let job = "Manger";
let salery = 0;
// if (job === "Manager") {
//   salary = 8000;
// } else if (job === "IT" || job === "Support") {
//   salary = 6000;
// } else if (job === "Developer" || job === "Designer") {
//   salary = 7000;
// } else {
//   salary = 4000;
// }                     make this in swich case
//       \|/
//       \|/
//       \|/
switch (job) {
  case "Manger":
    salery = 8000;
    break;
  case "IT":
  case "Support":
    salery = 6000;
    break;
  case "Developer":
  case "Designer":
    salery = 7000;
    break;
  default:
    salery = 4000;
    break;
}
console.log(`The salery of ${job} is ${salery}`);

// ----------------- array ----- ---- -- --- --- -//
let myfriend = ["mohamed", "Ahmad", "sayed", ["marwan", "mode"]];

console.log(
  myfriend[0][0].toUpperCase() + myfriend[0].substring(1, myfriend[0].length)
); // Mohamed

console.log(myfriend[2]);
console.log(myfriend[1]);
console.log(myfriend[3][1]);
// we know myfriend this is array
// but in JS this is type is object >> this false
// a true type is array
console.log(Array.isArray(myfriend)); // >> result is true
console.log(myfriend.length);

myfriend[2] = "ola"; // to change value in array
myfriend[myfriend.length] = "Ali"; // this add a elment
myfriend.length = 3; // you can limit a number of element
myfriend[6] = "moahmed";
console.log(myfriend);
// array output >> ["mohamed", "Ahmad", "sayed", ["marwan", "mode"] ,   ,   ,'mohamed' ]
// then number of length is  7 and index is 6
// creat newes indexs to arive a index 6 and make them emptys
// ----------
// can controle numbers of length in array
myfriend.length = 2;
// output  ["mohamed", "Ahmad"] >> index = 1 >> [   0   ,   1   ]
console.log(myfriend);
///
myfriend = ["mohamed", "Ahmad", "sayed", ["marwan", "mode"]];

myfriend.unshift("osama1", "osama2", "osama3");
// unshift add element at the start of array
console.log(myfriend);

myfriend.push("osama4", "osama5", "osama6");
// push add element at the end of array
console.log(myfriend);

let firstElement = myfriend.shift(); // this remove a frist element in array and return it
// and you can save this in element
// and this run when we save this in varuable
// this run untel use this varuable
console.log(myfriend);
console.log(`we use here shift to remove the first element ${myfriend}`);
console.log(`this is the first elemt in array ${firstElement}`);

let lastElement = myfriend.pop(); // this remove a end element in array and return it
// and you can save this in element
// and this run when we save this in varuable
// this run untel use this varuable
console.log(myfriend);
console.log(`we use here shift to remove the last element ${myfriend}`);
console.log(`this is the last elemt in array ${lastElement}`);
// ------------------------------ search in array ----- //
myfriend = ["mohamed", "Ahmad", "sayed", ["marwan", "mode"], "mohamed"];

console.log(myfriend.indexOf("mohamed")); // 0
console.log(myfriend.indexOf("mohamed", 2)); // 4
console.log(myfriend.lastIndexOf("mohamed")); // 4
console.log(myfriend.indexOf("mode")); // -1
// if result is -1 then isnot found

console.log(myfriend.includes("mohamed")); // true
// هى مثل الشرط و الناتج هو True , False

let myfriend1 = [
  100000,
  50,
  20,
  10,
  "10",
  100,
  9000,
  "mohamed",
  "Ahmad",
  "sayed",
  ["marwan", "mode"],
  "mohamed",
];

console.log(myfriend1);
// console.log(myfriend1.sort());
// ترتيب العناصر الترتيب الابجدىى للحرف و الترتيب المنطقى ل اول رقم فى كل رقم بغض النظر عن القيمه النهائيه للرقم
// 1000 >> 2 >> 3 >> 40 >> 5000 >> a >> b >> c >> d

// console.log(myfriend1.reverse()); // reverse a sort
// we can use

// console.log(myfriend1.sort().reverse()); // reverse a sort
// i will hide sort() becouse this save a new change and the next prosesing use that
console.log(myfriend1);
console.log(myfriend1.slice()); // this cut a part
console.log(myfriend1.slice(2, 5));
console.log(myfriend1.slice(-5));
myfriend1 = [
  100000,
  50,
  20,
  10,
  "10",
  100,
  9000,
  "mohamed",
  "Ahmad",
  "sayed",
  ["marwan", "mode"],
  "mohamed",
];

console.log(myfriend1);
// myfriend1.splice();
// splice >> splice( start, number element you well delete, elment you wont to add)
myfriend1.splice(0, 0, "Mohamed", "Ahmad");
console.log(myfriend1);
myfriend1.splice(0, 0, "Mohamed", "Ahmad");
console.log(myfriend1);

let allFreind = myfriend1.concat(myfriend, 1, [2552, "sayed"]);
// concat << this add (items or element) to array
console.log(allFreind);

myfriend1.splice(0, 0, myfriend);
console.log(myfriend1);
console.log(allFreind.join()); // Defolt is ,
// join this marge all element in array to string
console.log(allFreind.join("|").toUpperCase());

let zero = 0;
let counter = 3;
let my = ["Ahmed", "Mazero", "Elham", "Osama", "Gamal", "Ameer"];
// Write Code Here
// let my1 = my.slice(counter, my.length).splice(my1.l);
let my1 = my.slice(counter, my.indexOf("Ameer"));
let my2 = my.slice(zero, my.indexOf("Elham")).reverse();
let mytotla = my1.concat(my2);
console.log(my1);
console.log(my2);
console.log(mytotla); // ["Osama", "Elham", "Mazero", "Ahmed"]
my = ["Ahmed", "Mazero", "Elham", "Osama", "Gamal", "Ameer"];
// my.shift();
// my.pop();
// my.pop();
// my.pop();

// ["Osama", "Elham", "Mazero", "Ahmed"]
my = ["Ahmed", "Mazero", "Elham", "Osama", "Gamal", "Ameer"];
console.log(my.reverse().slice(counter, my.indexOf("Ahmad"))); // ["Elham", "Mazero"]
// ---------- looping---------------//
for (let i = 0; i == 10; i++) {
  console.log(i);
}

for (let i = 0; i < my.length; i++) {
  console.log(my[i]);
}
let mynama = [1, 2, 3, 5, "mohamed", "ahmad", 5582];
let newMyName = [];
for (let i = 0; i < mynama.length; i++) {
  if (typeof mynama[i] === "string") {
    newMyName.push(mynama[i]);
  }
}
console.log(newMyName);

let products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor"];
let colors = ["Red", "Green", "Black"];
let models = [2020, 2021];
console.log(products[0].length);
for (i = 0; i < products.length; i++) {
  console.log("#".repeat(15));
  console.log(`#### ${products[i]} #####`);
  //// a model loop
  for (K = 0; K < models.length; K++) {
    console.log(`-----${models[K]}`);
    //// a colores loop
    for (j = 0; j < colors.length; j++) {
      console.log(`--${colors[j]}`);
    }
  }
  console.log("#".repeat(15));
}
mmo = Math.min(...models);
console.log(mmo);

// loop control
// ####### break // containue // lapol
let main;
mainloopProductColor: for (i = 0; i < products.length; i++) {
  if (products[i] == "Pen") {
    continue;
  }
  let moo;
  document.write("#".repeat(15));
  document.write(
    `<p style="background:#ffaacc; width:fit-content;">#### ${products[i]} #####</p>`
  );
  //// a model loop
  for (K = 0; K < models.length; K++) {
    document.write(`<p>-----${models[K]}-----</p>`);
    //// a colores loop
    for (j = 0; j < colors.length; j++) {
      document.write(`--${colors[j]}`);
    }
  }
  document.write("# ".repeat(15));
  if (products[i] == "Pad") {
    break mainloopProductColor;
  }
}
// you can makea method in foe loop in anather position
let advansedLoop = 0;
for (;;) {
  console.log(products[advansedLoop]);
  advansedLoop++; // you can make any method
  if (advansedLoop == products.length) break;
}
// -----------while ------------//
i = 0;
products = ["Keyboard", "Mouse", "Pen", "Pad", "Monitor", "iPhone"];
while (products[i] != undefined) {
  /*hear if condition is true then loop dont stop*/ console.log(products[i]);
  i++;
  if (i === 3) break;
}
console.log("############");
// ----- do while -------- //
i = 0;
do {
  console.log(`${i} this do while in do `);
  i++;
} while (false);
console.log(`${i} this do while in do `);
// coding in do will be runing
// ------------ chalenge -------
let myAdmins = ["Ahmed", "Osama", "Sayed", "Stop", "Samera"];
let myEmployees = [
  "Amgad",
  "Samah",
  "Ameer",
  "Omar",
  "Othman",
  "Amany",
  "Samia",
  "Anwar",
];

document.write(`<hr>`);
document.write(`<p>we Have ${myAdmins.indexOf("Stop")} Admins</p>`);
document.write(`<p>we Have ${myEmployees.length} Admins</p>`);
document.write(`<hr>`);

let listNameEmp = [];
for (let k = 0; k < myAdmins.length; k++) {
  document.write(`<div>`);
  if (myAdmins[k] === "Stop") break;
  document.write(`The Admin For Team ${k + 1} Is ${myAdmins[k]}`);
  document.write(`<h3>Team Members:</h3>`);
  for (let j = 0; j < myEmployees.length; j++) {
    if (myAdmins[k].substring(0, 1) === myEmployees[j].substring(0, 1)) {
      listNameEmp.push(myEmployees[j]);
    }
  }
  console.log(listNameEmp);
  for (let q = 0; q < listNameEmp.length; q++) {
    document.write(`<p>- ${q + 1} ${listNameEmp[q]}</p>`);
  }
  listNameEmp = [];
  document.write(`</div>`);
  document.write(`<hr>`);
}
// ---- function ---- // pascal teringle
function mo(name, age) {
  age = age || "unknown";
  if (age < 20) {
    console.log(`App is not Suitable for you `);
  } else {
    console.log(`hallo ${name} age : ${age}`);
  }
}
function mo1(name, age = "unknown" /*anew way to return anuther value*/) {
  if (age < 20) {
    console.log(`App is not Suitable for you `);
  } else {
    console.log(`hallo ${name} age : ${age}`);
  }
}
mo("mohamed", 40); // output is hallo mohamed age : undefine
mo("ahmad", 19); // output is hallo mohamed age : 19

// return in function
// >>>> this is stop a code in function
function generate(start, end) {
  for (let i = start; i <= end; i++) {
    if (i === 15) {
      return `Interruptting`;
    }
    console.log(i);
  }
}
generate(10, 20);
console.log("#######################");

// rest paramiters
function calc(...number) {
  let s = 0;
  /*(...) this make number a (array) and you can add any number of input*/
  for (let f = 0; f < number.length; f++) {
    console.log(number[f]);
    s += number[f];
  }
  return `Final result  is ${s}`;
}
console.log(calc(10, 20, 30, 40, 45, 30));

function showinfo(
  name = "unknown",
  age = "ageunknown",
  rt = 0,
  show = "yas",
  ...skiles
) {
  document.write(`<div id='mo'>`);
  document.write(`    <h3>Welcome ${name}</h3>`);
  document.write(`    <p>your information :</p>`);
  document.write(`    <p>--Age: $${age}</p>`);
  document.write(`    <p>--Hour rate: ${rt}</p>`);
  if (show == "yas") {
    if (skiles.length > 0) {
      document.write(`<p>--shiles: </p>`);
      for (i = 0; i < skiles.length; i++) {
        document.write(`<p>----${skiles[i]}</p>`);
      }
    }
    else {
      document.write(`<p>--shiles: No skiles</p>`);
    }
  } 
  else {
    console.log("     <p>--skiles is hidden</p>");
  }

  document.write(`</div>`);
}

showinfo("Mohamed", 20, 50, "yas", "html", "CSS", "JS");
let names;
let bols;
let ages, final_boll;

// ---------- chalange ------//
function showdet(a, b, c) {
  names = typeof a === "string" ? a : typeof b === "string" ? b : c;
  bols = typeof a === "boolean" ? a : typeof b === "boolean" ? b : c;
  ages = typeof a === "number" ? a : typeof b === "number" ? b : c;
  final_boll = bols === true ? "Are" : "Are Not";
  console.log(typeof a);
  console.log(typeof b);
  console.log(bols);
  document.write(
    `<div>Hallo ${names}, Your Age Is ${ages}, You ${final_boll} Available For Hire</div>`
  );
}
showdet("Mohamed", 16, true);

//make a function in error this name is anonymous >> not use name
let calculat = function (num1, num2) {
  return num1 + num2;
};

console.log(calculat(1, 2));

// let mo = document.querySelector("input").value;
function start() {
  var start1 = +document.getElementById("one1").value;
  var start2 = +document.getElementById("one2").value;
  var sum = start1 + start2;
  console.log(sum);
  document.getElementById("sum").value = sum;
  document.getElementById("-sum").value = start1 - start2;
  document.getElementById("product").value = start1 * start2;
}

////////////////.....Scope....////////////////
var x125 = 1 ;
let y125 = 2 ;
function show125(){
  x125 = 10 ;
  y125 = 20 ;
  console.log(`function - from local ${x125}`)
  console.log(`function - from local ${y125}`)
} 
show125();
console.log(`from local ${x125}`);
console.log(`from local ${y125}`);


//// in (if)  
let x126 = 0

if (10 === 10 ){
  x126 = 100
}
console.log(x126)
function parent(){
  let a = 10 ;
  function chiled(){
    let a = 8 ;
    console.log(a);
    function grand(){
    
    }
  }
  chiled();
}

parent();

////// challenge ////////
maka = [0,1,2,3,3,5,4,4,5,6]
let names1 = (...arguments) => `String [${arguments.join('],[')}] => Done !`;

console.log(names1 ("Osama", "Mohamed", "Ali", "Ibrahim"));
// String [Osama], [Mohamed], [Ali], [Ibrahim] => Done !


let myNumbers= [20, 50, 10, 60];
let calc1 = (one, two, ... nums) =>one +two/5 + nums.reduce((a, b) => a + b);
console.log(calc1(10, 50, 60)); // 80

/////////////// Height Order Function ///////////////
//// - Map -- method for array -- make operation in a new array ,not in original array
let myNums = [1, 2, 3, 4, 5, 6];
let newArray = [] ;
let addSelf = myNums.map((element) => element * element );
console.log(addSelf);  
////// some quition //////

let swappingCases = "elZERO";
let sw = swappingCases.split('').map((element)=>element==element.toUpperCase()?element: element.toUpperCase()).join("")
console.log(sw)

let invertedNumbers = [1, -10, -20, 15, 100, -30];
let invertnumber = invertedNumbers.map((number)=>-number)
console.log(invertnumber)

let ignorenumber = "Elz123er40o";

let ignorenumber1 = ignorenumber.split("").map((ele)=> isNaN(ele) ? ele:'' ).join('') ;
console.log(ignorenumber1)

/////// Filter //////// 
//// this is like map , but this return a element is accpet in condition (filter)
/// For Example
// Get Friends With Name Starts With A
let friends = ["Ahmed", "Sameh", "Sayed", "Asmaa", "Amgad", "Israa"];
// Get Even Numbers Only
let numbers = [11, 20, 2, 5, 17, 10];

let Filtaring_string = friends.filter((ele)=> ele.startsWith("A"));
let Filtaring_number = numbers.filter((ele)=> ele%2 == 0 );
console.log(Filtaring_string)
console.log(Filtaring_number)

//////// mix map and filter ////////

// Filter Words More Than 4 Characters
let sentence = "I Love Foood Code Too Playing Much";
let new_entance = sentence.split(' ').filter((ele)=>ele.length<=4).join(' ');
console.log(new_entance)

// Filter-Strings + Multiply

let mix = "A13BS2ZX";
let result_number =1; 
let result_string =''; 
mix.split('').map((ele) =>isNaN(ele)?result_string+=ele:result_number*=ele) ;
console.log(result_string ,'+', result_number) ;

// return each number * the same number
console.log( mix.split('').filter(function(ele){
  return !isNaN(ele);
}).map((ele)=>ele*ele))
// or 
console.log( mix.split('').map((ele)=>!isNaN(ele)?ele*ele:""))
// Reduce // minmize all result to return one result  reduce (function,initial value )
// initial value >> is a start point , is this is valed then accomlator(return_value) = initial value
let nums_reduce= [10,20,15,30];
let Reduc_1 = nums_reduce.reduce(function(return_number , current , index,arr){
  console.log(`Acc => ${return_number}`);
  console.log(`Current Element => ${current}`);
  console.log(`Current Element Index -> ${index}`);
  console.log(`Array => ${arr}`);
  console.log(return_number + current);
  console.log(`#############`);
  return return_number + current;
})

console.log(Reduc_1)
// challenge 

let theBiggest = ["Bla", "Propaganda", "Other", "AAA", "Battery", "Test", "Propaganda+tow"];
let check = theBiggest.reduce(function (acc, current) {

  return acc.length > current.length ? acc : current;
  });
  // return then longers word 
  console.log(check)

  let removeChars = ["E", "@", "@", "L", "Z", "@", "@","E","R", "@", "O"];
let final_after_remove  = removeChars.filter(element=>element=='@'?'':element).reduce(function(return_,current){
  return return_+current
})
console.log(final_after_remove)
let final_after_remove_2 = removeChars.reduce((crr,curent)=>curent!="@"?crr+=curent:crr)
console.log(final_after_remove_2)


// filter , map , reduce this return a new list
// forEach // that is edite the mane list and dont return 
let list_In_html = document.querySelectorAll("ul li")
let DIv_In_html = document.querySelectorAll(".continer div")

list_In_html.forEach(function(elle){
  elle.onclick = function(elle){
    list_In_html.forEach(function(elle){
      elle.classList.remove("active")
    })
    this.classList.add('active')
    DIv_In_html.forEach(function(ele){
      ele.style.display= 'none';
    })
  }
})
// Higher order Function Challenge 

let myString = "1,2,3,EE,l,z,e,r,o,_,W,e,b,_,S,c,h,o,o,l,2,0,Z";
let solution_reduce ='?????';
let solution_map ='?????';
let solution_filter ='?????';
solution_reduce = myString.split(',').reduce(function(return_,curr){
  return curr == '_'?return_+=' ':isNaN(curr) ?return_+=curr: return_;
},'')

console.log('reduce'); // Elzero Web School
console.log(solution_reduce); // Elzero Web School

solution_filter = myString.split(',').filter(function(ele){
  return isNaN(ele) 
}).join('').replaceAll('_',' ')

console.log('filter'); // Elzero Web School
console.log(solution_filter); // Elzero Web School
let solution_map_string = ' '
solution_map = myString.split(',').map(function(ele){
  return isNaN(ele) ? ele : ele == "_" ? ' ':""; 
}).join('')
console.log('map'); // Elzero Web School
console.log(solution_map); // Elzero Web School

// ForEach
// not make a new array
// this is make a operation in the same array
// this make a operation in all element in array
// this is not return a new array
// this is not return a value
// بيطبق على كل عنصر فى الاراى و بيعمل عليه عملية معينة

let foreach_list = document.querySelectorAll("ul li");

foreach_list.forEach(function(ele) {
  ele.onclick = function () {
    foreach_list.forEach(function(ele) {
      ele.classList.remove("active");
    });
    this.classList.add("active");
  };
});


/////  object

let user_myObject = {
  thename: "Mohamed",
  theage: 20,
  country: "Egypt",
  //methods
  sayHallo: function () {
    return `Hallo ${this.thename}`;
  },
};
console.log(user_myObject.thename);
console.log(user_myObject.theage);
console.log(user_myObject.sayHallo());

let myVar = "country";
let user = {
theName: "Osama",
country: "Egypt",
};
console.log(user.theName);
console.log(user.country); // user.country
console.log(user.myVar); // user.country
console.log(user [myVar]); // user.country