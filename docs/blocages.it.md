# Quando qualcosa non funziona

Le situazioni che si incontrano davvero, con la loro causa e cosa fare. Quasi tutte hanno la
stessa origine: **una condizione posta a monte non è soddisfatta**, e la schermata rifiuta
invece di indovinare.

## Lato studente

### «Non vedo nessuna campagna»

Tre cause possibili, in quest'ordine di frequenza.

**La campagna non è aperta.** Solo lo stato **Aperta** accetta preferenze. Una campagna
«Pronta» è visibile a voi, non ai vostri studenti.

**Lo studente non fa parte del bacino.** I criteri della campagna — livello, percorso,
campus, etichette, filtri — non lo trattengono. Aprite la campagna e guardate l'elenco dei
partecipanti: se non c'è, aggiungetelo a mano.

**Lo studente non ha un profilo.** Senza pratica, non esiste per nessuna campagna.

### «Non riesco a convalidare le mie preferenze»

Avete fissato un **minimo di preferenze** e non l'ha raggiunto. Il minimo blocca quanto il
massimo.

### «Non trovo nessuna destinazione»

Il bacino di destinazioni della campagna è vuoto, oppure nessun posto è collocato sugli
accordi che trattiene. Verificate la matrice dei posti prima di cercare altrove: una
destinazione senza posti non compare.

Verificate anche il **periodo**: un posto esiste sempre per un periodo dato.

### «Non vedo più la mia classifica»

È voluto, se il vostro istituto ha nascosto la classifica agli studenti. L'impostazione è in
[Cosa vedono i vostri studenti](etablissement/parametres.md) — voi e il vostro team
continuate a vederla.

### «Non ho ricevuto i miei accessi»

Un accesso aperto non è un accesso ricevuto. Guardate la colonna di stato dell'accesso nel
vostro elenco studenti: dice se è partito e quando. E la colonna **Connected** dice se si è
già collegato — sono due domande diverse.

## Lato campagna

### «Il turno di assegnazione si rifiuta di partire»

È il blocco più frequente, ed è sempre spiegato: il resoconto **nomina** gli studenti che
bloccano e la ragione.

| Messaggio | Cosa fare |
|---|---|
| Lo studente non ha **percorso** | Collegatelo a un percorso. Se il vostro istituto non ne usa, createne uno per livello. |
| Lo studente non ha **classifica** | Importate la classifica prima di rilanciare. Il turno non la fabbrica. |
| Lo studente non ha **profilo** | Non c'è nulla da collocare. |
| La sua **pratica è incompleta** | Completatela, o impostate la campagna su «segnalare» anziché «bloccare». |

!!! tip "Il turno non è un gesto unico"
    Correggete ciò che blocca e rilanciatelo tutte le volte che serve.

### «Non riesco a eliminare questa campagna»

Si elimina solo una campagna in **bozza**. Una campagna aperta porta già delle preferenze.

### «Non riesco a riaprire questa campagna»

Si riapre solo una campagna **terminata**. E se la riaprite senza spostare la data di fine, si
richiuderà già il mattino dopo.

### «La mia campagna si è chiusa da sola»

La sua data di fine è passata. È il funzionamento normale da settembre 2026: il giorno dopo
l'ultimo giorno la campagna si chiude, le preferenze in bozza diventano preferenze e voi
ricevete il bilancio. Riapritela e spostate la data se era prematuro.

### «I miei contatori dei posti non dicono la stessa cosa dell'esportazione»

Da settembre 2026, tutti i contatori dei posti riguardano solo le mobilità **in uscita** —
quelle che inviate voi. I posti che i vostri partner aprono da loro non gonfiano più i vostri
totali. Se una cifra vi sorprende, probabilmente era sbagliata prima.

## Lato partner

### «Non riesco a sollecitare questo partner»

Una sollecitazione ogni ventiquattro ore. Il pulsante si disattiva dopo, e vi dirà quando.

### «Non riesco a nominare questo studente su questo accordo»

C'è già una nomina in corso su quell'accordo per lui. Ritiratela prima, se volete rifarla.

### «Questo partner non compare nella mia campagna»

Il bacino di destinazioni non lo trattiene: verificate i tipi di accordo, i periodi e i
filtri di istituto della campagna. Verificate anche che non sia archiviato o nascosto.

### «Non riesco a rifiutare questa nomina»

Un rifiuto richiede un motivo. Sarà trasmesso all'istituto che vi ha nominato lo studente.

## Lato accessi e permessi

### «Questa schermata è in sola lettura»

Il vostro ruolo vi dà il livello **Consultare** su questa sezione. Un banner lo dice in alto.
La vostra schermata [I miei permessi](etablissement/parametres.md) vi dice esattamente cosa
potete fare e su chi.

### «Questo studente è fuori dal mio perimetro»

Il vostro ruolo è limitato a una direzione, un campus o delle coorti che non lo coprono. Non è
un guasto: è il perimetro definito dal vostro amministratore.

### «Una parte della mia selezione non è stata trattata»

La vostra azione riguardava righe fuori dal vostro perimetro. Vengono messe da parte, e la
schermata vi dice quali.

### «Non riesco ad accedere con l'account del mio istituto»

Il single sign-on verifica **chi siete**, non decide che avete il diritto di entrare. Il
vostro account deve esistere già in AroundLink. Si veda
[Chi fornisce cosa](plateforme/sso-microsoft.md).

## Lato documenti

### «Non riesco a salvare questo punteggio linguistico»

Un punteggio richiede sempre un giustificativo. Il file e la data sono obbligatori.

### «Mi viene chiesto un motivo per modificare il learning agreement»

Ogni componente aggiunto o rimosso dopo la convalida richiede una giustificazione. È
un'esigenza del contratto, non un'impostazione.
