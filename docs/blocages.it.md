# Quando qualcosa non funziona

Le situazioni che si incontrano davvero, con la loro causa e cosa fare. Quasi tutte hanno la
stessa origine: **una condizione posta a monte non è soddisfatta**, e la schermata rifiuta
invece di indovinare.

## Lato studente

### «Non vedo nessuna campagna»

Tre cause possibili, in quest'ordine di frequenza.

**La campagna è ancora in bozza.** Uno studente vede una campagna **Pronta**, **Aperta** o
**Terminata** — mai una **Bozza**. Solo **Aperta** accetta preferenze.

**Lo studente non fa parte del bacino.** I criteri della campagna — livello, anno
accademico, etichetta di livello, campus, tag, filtri — non lo trattengono, oppure ha già
un'assegnazione. Aprite la campagna e guardate l'elenco dei partecipanti: se non c'è,
aggiungetelo a mano.

**Lo studente non ha un profilo.** Senza pratica, non esiste per nessuna campagna.

### «Non riesco a convalidare le mie preferenze»

Avete fissato un **minimo di preferenze** e non l'ha raggiunto: il suo elenco non viene
salvato. Il minimo blocca quanto il massimo. Il messaggio che riceve indica anche cosa manca
per una destinazione — un punteggio linguistico, un documento.

### «Non trovo nessuna destinazione»

Lo studente vede solo le destinazioni in cui un posto è **pianificato per lui**: la sua riga
della matrice — anno, livello, etichetta di livello, periodo. Verificate la matrice dei posti
prima di cercare altrove.

Restano esclusi anche: i partner nascosti o archiviati, il suo stesso campus, e i partner i
cui **filtri studenti** non corrispondono ai suoi — quando sia lo studente sia il partner
hanno dei filtri, devono averne almeno uno in comune.

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

Il resoconto **nomina** gli studenti che bloccano e la ragione. Tre ragioni impediscono
l'avvio:

| Messaggio | Cosa fare |
|---|---|
| **no student record** | Non c'è nulla da collocare. |
| **no level track** | Collegatelo a un'etichetta di livello (*Custom level*). Se il vostro istituto non ne usa, createne una per livello. |
| **no imported class rank** | Importate la classifica prima di rilanciare. Il turno non la produce. |

Una **pratica incompleta** non impedisce l'avvio. Se la campagna è impostata su **Block the
assignment until everything is in hand**, lo studente viene messo da parte e nominato nel
resoconto; con **Show it, assign anyway (recommended)**, viene collocato e segnalato. Gli
studenti che hanno risposto «non desidero partire» non bloccano mai.

!!! tip "Il turno non è un gesto unico"
    Correggete ciò che blocca e rilanciatelo tutte le volte che serve.

### «Non riesco a eliminare questa campagna»

Si elimina solo una campagna in **bozza**. Una campagna aperta porta già delle preferenze.

### «Non riesco a riaprire questa campagna»

Si riapre solo una campagna **terminata**. Se la riaprite dopo l'ora di chiusura, **resta
aperta** finché non la chiudete voi: la chiusura automatica non la richiude.

### «La mia campagna si è chiusa da sola»

La sua ora di chiusura è passata: la campagna si chiude al minuto che avete fissato, le
preferenze vengono congelate e voi ricevete il bilancio. Riapritela se era prematuro.

### «I miei contatori dei posti non dicono la stessa cosa dell'esportazione»

I contatori dei posti riguardano le mobilità **in uscita** — quelle che inviate voi. I posti
che i vostri partner aprono da loro non gonfiano i vostri totali; l'accordo li mostra a
parte, in un indicatore delle mobilità in entrata.

## Lato partner

### «Non riesco a sollecitare questo partner»

Una sollecitazione ogni ventiquattro ore. Dopo, il pulsante si disattiva e il suo tooltip
indica la data dell'ultima sollecitazione.

### «Non riesco a nominare questo studente su questo accordo»

Due cause. **Nessun contatto presso questo partner**: "No contact for this partner — add one
to be able to nominate." Aggiungete un contatto sulla sua scheda. **Lo studente è già
nominato**: si può nominare solo un'assegnazione non ancora nominata. Per ricominciare,
ritirate la nomina, poi assegnatelo di nuovo.

### «Questo partner non compare nella mia campagna»

Il bacino di destinazioni non lo trattiene: verificate i tipi di accordo, i periodi, il
livello, l'anno accademico, il tipo di mobilità e i filtri di istituto della campagna, e che
l'accordo sia attivo. Verificate anche che non sia archiviato o nascosto.

### «Non riesco a rifiutare questa nomina»

Un rifiuto richiede un motivo. Sarà trasmesso all'istituto che vi ha nominato lo studente.

## Lato accessi e permessi

### «Questa schermata è in sola lettura»

Il vostro ruolo vi dà il livello **View** su questa sezione. Un banner lo indica in alto
nella schermata. La vostra schermata [I miei permessi](etablissement/parametres.md) vi dice
esattamente cosa potete fare e su chi.

### «Questo studente è fuori dal mio perimetro»

Il vostro ruolo è limitato a un ambito di attività, una direzione, un campus o delle coorti
che non lo coprono. Non è un guasto: è il perimetro definito dal vostro amministratore.

### «Una parte della mia selezione non è stata trattata»

La vostra azione riguardava righe fuori dal vostro perimetro. Vengono messe da parte, e la
schermata vi dice quante sono.

### «Non riesco ad accedere con l'account del mio istituto»

Il single sign-on verifica **chi siete**, non decide che avete il diritto di entrare. Il
vostro account deve esistere già in AroundLink. Si veda
[Chi fornisce cosa](plateforme/sso-microsoft.md).

## Lato documenti

### «Non riesco a salvare questo punteggio linguistico»

Un punteggio richiede sempre un giustificativo. Quando è lo studente stesso a inserirlo,
anche la data del test è obbligatoria.

### «Mi viene chiesto un motivo per modificare il learning agreement»

Ogni componente aggiunto o rimosso dopo la convalida richiede una giustificazione. È
un'esigenza del contratto, non un'impostazione.
