/**
 * Propose un rendez-vous après quelques pages lues.
 *
 * Quelqu'un qui ouvre une page cherche une réponse ; quelqu'un qui en ouvre quatre a un
 * projet. On attend donc le quatrième avant de proposer quoi que ce soit — et on ne
 * repropose jamais à qui a fermé la fenêtre.
 *
 * Tout tient dans le navigateur du lecteur : rien n'est envoyé, rien n'est mesuré.
 */
(function () {
  "use strict";

  var SEUIL = 4;
  var LIEN = "https://cal.com/simon-petit-aroundlink/30minds";
  var CLE_PAGES = "al-pages-lues";
  var CLE_VUE = "al-rdv-ferme";

  var T = {
    fr: { titre: "Une question sur votre cas ?",
          texte: "Trente minutes avec notre équipe pour parler de votre établissement, de vos accords et de votre organisation — plutôt que de chercher la réponse page par page.",
          oui: "Réserver trente minutes", non: "Continuer la lecture" },
    en: { titre: "A question about your own case?",
          texte: "Thirty minutes with our team to talk about your institution, your agreements and your way of working — rather than hunting for the answer page by page.",
          oui: "Book thirty minutes", non: "Keep reading" },
    es: { titre: "¿Una pregunta sobre su caso?",
          texte: "Treinta minutos con nuestro equipo para hablar de su institución, de sus acuerdos y de su organización — en lugar de buscar la respuesta página por página.",
          oui: "Reservar treinta minutos", non: "Seguir leyendo" },
    it: { titre: "Una domanda sul vostro caso?",
          texte: "Trenta minuti con il nostro team per parlare del vostro istituto, dei vostri accordi e della vostra organizzazione — invece di cercare la risposta pagina per pagina.",
          oui: "Prenotare trenta minuti", non: "Continuare a leggere" },
    de: { titre: "Eine Frage zu Ihrem Fall?",
          texte: "Dreißig Minuten mit unserem Team über Ihre Hochschule, Ihre Abkommen und Ihre Arbeitsweise — statt die Antwort Seite für Seite zu suchen.",
          oui: "Dreißig Minuten buchen", non: "Weiterlesen" }
  };

  function langue() {
    var l = (document.documentElement.lang || "fr").slice(0, 2).toLowerCase();
    return T[l] ? l : "fr";
  }

  // Un navigateur privé, ou un stockage refusé, ne doit pas casser la page.
  function lire(cle, defaut) {
    try { var v = window.localStorage.getItem(cle); return v === null ? defaut : v; }
    catch (e) { return defaut; }
  }
  function ecrire(cle, valeur) {
    try { window.localStorage.setItem(cle, valeur); } catch (e) { /* tant pis */ }
  }

  function ouvrir() {
    var t = T[langue()];
    var fond = document.createElement("div");
    fond.className = "al-rdv-fond";
    fond.innerHTML =
      '<div class="al-rdv" role="dialog" aria-modal="true" aria-labelledby="al-rdv-titre">' +
        '<button class="al-rdv-x" type="button" aria-label="Fermer">&times;</button>' +
        '<h2 id="al-rdv-titre">' + t.titre + "</h2>" +
        "<p>" + t.texte + "</p>" +
        '<p class="al-rdv-actions">' +
          '<a class="al-rdv-oui" href="' + LIEN + '" target="_blank" rel="noopener">' + t.oui + "</a>" +
          '<button class="al-rdv-non" type="button">' + t.non + "</button>" +
        "</p>" +
      "</div>";
    document.body.appendChild(fond);

    function fermer() {
      ecrire(CLE_VUE, "1");
      if (fond.parentNode) { fond.parentNode.removeChild(fond); }
      document.removeEventListener("keydown", surTouche);
    }
    function surTouche(e) { if (e.key === "Escape") { fermer(); } }

    fond.querySelector(".al-rdv-x").addEventListener("click", fermer);
    fond.querySelector(".al-rdv-non").addEventListener("click", fermer);
    // Un clic sur le lien vaut réponse : on ne lui repropose pas au prochain passage.
    fond.querySelector(".al-rdv-oui").addEventListener("click", function () { ecrire(CLE_VUE, "1"); });
    fond.addEventListener("click", function (e) { if (e.target === fond) { fermer(); } });
    document.addEventListener("keydown", surTouche);
    fond.querySelector(".al-rdv-x").focus();
  }

  /* ---------- le bouton de l'en-tête ---------- */

  var LIBELLE = {
    fr: "Prendre rendez-vous", en: "Book a meeting", es: "Reservar una cita",
    it: "Prenota un incontro", de: "Termin buchen"
  };

  function poserBouton() {
    var barre = document.querySelector(".md-header__inner");
    if (!barre || document.querySelector(".al-rdv-entete")) { return; }
    var a = document.createElement("a");
    a.className = "al-rdv-entete";
    a.href = LIEN;
    a.target = "_blank";
    a.rel = "noopener";
    a.textContent = LIBELLE[langue()] || LIBELLE.fr;
    // Juste avant la recherche, là où vivait la bascule de thème.
    var recherche = barre.querySelector(".md-header__option, [data-md-component=search], .md-search");
    if (recherche) { barre.insertBefore(a, recherche); } else { barre.appendChild(a); }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", poserBouton);
  } else {
    poserBouton();
  }

  if (lire(CLE_VUE, "") === "1") { return; }

  var vues = parseInt(lire(CLE_PAGES, "0"), 10) || 0;
  vues += 1;
  ecrire(CLE_PAGES, String(vues));

  // Laisser la page s'installer avant de la recouvrir.
  if (vues >= SEUIL) { window.setTimeout(ouvrir, 1200); }
})();
