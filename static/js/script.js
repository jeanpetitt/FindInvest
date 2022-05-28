// fonctions utiles lors de la validation des formulaires

function valChapmsQuestRepons(champs, errClass, contain) {
    if (champs.value == "") {
      errClass.innerHTML="*veuillez entrer une question et une réponse";
      champs.focus();
      contain.classList.add('err');
      return false;
    } else {
      errClass.innerHTML="";
      contain.classList.remove('err');
      return true;
    }
}
function valChapmsText(champs, errClass) {
    if (champs.value == "") {
      errClass.innerHTML="*veuillez remplir ce champs";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else {
      errClass.innerHTML="";
      champs.classList.remove('err');
      return true;
    }
}
function valChapmsSelect(champs, errClass) {
    if (champs.value == "") {
      errClass.innerHTML="*veuillez choisir un élément de la liste";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else {
      errClass.innerHTML="";
      champs.classList.remove('err');
      return true;
    }
}
function valChapmsAge(champs, errClass) {
    if (champs.value == "") {
      errClass.innerHTML="*veuillez entrer un nombre";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else if (champs.value <= "0" || champs.value >= "50") {
      errClass.innerHTML="*entrez un âge correct (<50)";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else {
      errClass.innerHTML="";
      champs.classList.remove('err');
      return true;
    }
}
function valChapmsEmail(champs, errClass) {
    var valeursAcceptees = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
    if (champs.value == "") {
      errClass.innerHTML="*veuillez entrer une addrese mail";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else if ( ! champs.value.match(valeursAcceptees)) {
      errClass.innerHTML="*veuillez entrer une addrese mail valide";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else {
      errClass.innerHTML="";
      champs.classList.remove('err');
      return true;
    }
}
function valChapmsTel(champs, errClass) {
    if (champs.value == "") {
      errClass.style.display="";
      errClass.innerHTML="*veuillez entrer un numéro correct";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else if (champs.value.charAt(0)!="+") {
      errClass.style.display="";
      errClass.innerHTML="*indicatif du pays manquant, ex: +237";
      champs.focus();
      champs.classList.add('err');
      return false;
    } else if (champs.value.length <= 11 || champs.value.length >= 16) {
      errClass.style.display="";
      errClass.innerHTML="*veuillez entrer un numéro correct (11 chiffres minimum)";
      champs.focus();
      champs.classList.add('err');
      return false;
    }  else {
      for (let i = 1; i < champs.value.length; i++) {
        if (champs.value.charAt(i) < "0" || champs.value.charAt(i) > "9") {
          errClass.style.display="";
          errClass.innerHTML="*veuillez entrer un numéro correct";
          champs.focus();
          champs.classList.add('err');
          return false;
        }
      }
    }
    
    errClass.innerHTML="";
    champs.classList.remove('err');
    return true;
    
}

// inscription Etudiant etape 1

var last_nameEtu = document.getElementById('id_last_name');
var error_last_nameEtu = document.getElementById('error_last_nameEtu');

var villeEtu = document.getElementById('id_ville');
var error_villeEtu = document.getElementById('error_villeEtu');

var univEtu = document.getElementById('id_universite');
var error_univEtu = document.getElementById('error_univEtu');

var telephoneEtu = document.getElementById('id_telephone');
var error_telephoneEtu = document.getElementById('error_telephoneEtu');

function valEtu1() {
    if (valChapmsText(last_nameEtu, error_last_nameEtu)
        && valChapmsText(univEtu, error_univEtu)
        && valChapmsText(villeEtu, error_villeEtu)
        && valChapmsTel(telephoneEtu, error_telephoneEtu)) {
        return true;
    } else {
        return false;
    }
}

//  valider et passer à l'étape 2

const suivantBtnEtu = document.querySelector('.suivantBtnEtu');
const precedentBtn = document.querySelector('.precedentBtn');
const formBx = document.querySelector('.formBx');
const body = document.querySelector('body');

suivantBtnEtu.onclick = function() {
    if (valEtu1()) {
        formBx.classList.add('active');
        body.classList.add('active');
    }
}
precedentBtn.onclick = function() {
    formBx.classList.remove('active');
    body.classList.remove('active');
}

// inscription Etudiant etape 2

var emailEtu = document.getElementById('id_email');
var error_emailEtu = document.getElementById('error_emailEtu');

var questtionEtu = document.getElementById('id_question');
var reponseEtu = document.getElementById('id_reponse');
var error_questionEtu = document.getElementById('error_questionEtu');

var quest_rep = document.getElementById('quest_rep')

function valEtu2() {
    if (valChapmsEmail(emailEtu, error_emailEtu)
        && valChapmsQuestRepons(questtionEtu, error_questionEtu, quest_rep)
        && valChapmsQuestRepons(reponseEtu, error_questionEtu, quest_rep)) {
        return true;
    } else {
        return false;
    }
}

function validateFormEnreg() {
    var usernam = document.getElementById('id_username');
    var email = document.getElementById('id_email');
    usernam.value = email.value
    if (valEtu1()) {
        formBx.classList.add('active');
        body.classList.add('active');
    }
    return valEtu1()&&valEtu2();
}



// inscription INVESTISSEUR etape 1

// var professionInv = document.getElementById('id_profession');
// var error_professionInv = document.getElementById('error_professionInv');

// var objectifsInv = document.getElementById('id_objectifs');
// var error_objectifsInv = document.getElementById('error_objectifsInv');

// function valInv1() {
//     if (valChapmsText(last_nameEtu, error_last_nameEtu)
//         && valChapmsText(professionInv, error_professionInv)
//         && valChapmsText(objectifsInv, error_objectifsInv)
//         && valChapmsText(villeEtu, error_villeEtu)
//         && valChapmsTel(telephoneEtu, error_telephoneEtu)) {
//         return true;
//     } else {
//         return false;
//     }
// }

//  valider et passer à l'étape 2

// const suivantBtnInv = document.getElementById('suivantBtnInv');
// suivantBtnInv.onclick = function() {
    // if (valInv1()) {
    //     formBx.classList.add('active');
    //     body.classList.add('active');
    // }
//     alert("salut");
// }

// inscription INVESTISSEUR etape 2

    // pareil que l'etape 2 de l'inscrition étudiant