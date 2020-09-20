# Kehonkoostumuspäiväkirja (ja harjoituspäiväkirja)

Harjoitustyönä tehtävä tietokantasovellus, jonka avulla voi seurata oman kehon kunnon muutoksia erilaisilla mittareilla. Aluksi luodaan luodaan mittaristo ja raportit kehonkoostumuksen seuraamiseen. Myöhemmin lisätään mahdollisuus harjoitussuoritusten tallettamiseen ja tarkasteluun.

[Linkki raakilesovellukseen](https://tsoha-kehokuntoon.herokuapp.com/)

Fuksiläppärittömyys tuotti jälleen harmaita hiuksia ja tunteja kului etenkin PostgreSQL:n asennuksessa. Kurssin ohjeistuksen tulisi ottaa paremmin huomioon se, ettei kaikilla ole fuksiläpäriä tai vahvaa kokemusta Linux-ympäristöstä.

* Sovelluksella voi seurata monipuolisesti harjoittelua ja kehon tilaa 
* Käyttäjä voi olla peruskäyttäjä, ryhmänvetäjä tai ylläpitäjä
* Käyttäjä voi luoda tunnuksen perustietoineen
  * Pituus, paino ovat pakolliset
  * Vatsanympärys, verenpaine, lihas- ja rasva-%, jos ovat tiedossa
* Käyttäjä voi lisätä päivittäiset mittaustulokset
  * Paino on ainoa pakollinen kirjattava tieto, jos ei anneta uutta merkitään edellinen kirjattu paino
  * Muut päivittäiset kirjaukset ovat vapaaehtoisia
  * Käyttäjä voi luoda itselleen järkevän painotavoitteen (BMI alipainoa ei hyväksytä)
* Käyttäjä voi lisätä päivälle useita treenejä
  * Treeni voi olla lihaskunto- tai kestävyyskuntoharjoitus
  * Harjoituksen pituus voidaan ilmoittaa joko mm:ss tai aloitus- ja lopetusaikana
  * Halutessaan voi lisätä maksimi- ja keskisykkeen
* Käyttäjä luoda ryhmän yhteisten treenien kirjaamiseen
  * Tällöin käyttäjä saa ryhmänvetäjän oikeudet
  * Ryhmänvetäjä voi tarkastella ryhmään kirjattuja harjoituksia
* Harjoituksia voi poistaa ja päivän mittaustietoja voi korjata
* Päiväkirjoja, joihin on oikeuspäästä, voi selata kalenterinäkymässä
* Harjoituksista ja mittauksista voi luoda yhteenvetoja
