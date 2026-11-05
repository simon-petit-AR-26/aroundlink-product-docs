# Cuando algo no funciona

Las situaciones que se encuentran de verdad, con su causa y qué hacer. Casi todas tienen el
mismo origen: **una condición fijada antes no se cumple**, y la pantalla se niega en lugar de
adivinar.

## Del lado del estudiante

### «No veo ninguna campaña»

Tres causas posibles, en este orden de frecuencia.

**La campaña sigue en borrador.** Un estudiante ve una campaña **Lista**, **Abierta** o
**Terminada** — nunca una en **Borrador**. Solo **Abierta** acepta preferencias.

**El estudiante no forma parte del grupo.** Los criterios de la campaña — nivel, año
académico, denominación de nivel, campus, etiquetas, filtros — no lo retienen, o ya tiene una
asignación. Abra la campaña y mire la lista de participantes: si no está, añádalo a mano.

**El estudiante no tiene perfil.** Sin expediente, no existe para ninguna campaña.

### «No puedo validar mis preferencias»

Usted ha fijado un **mínimo de preferencias** y el estudiante no lo ha alcanzado: su lista no
se guarda. El mínimo bloquea tanto como el máximo. El mensaje que recibe indica también lo que
le falta para un destino — un resultado de idioma, un documento.

### «No encuentro ningún destino»

El estudiante solo ve los destinos en los que hay una plaza **prevista para él**: su fila de
la matriz — año, nivel, denominación de nivel, semestre. Compruebe la matriz de plazas antes de
buscar en otra parte.

También quedan excluidos: los socios ocultos o archivados, su propio campus, y los socios cuyos
**filtros de estudiantes** no coinciden con los suyos — cuando tanto el estudiante como el
socio tienen filtros, deben compartir al menos uno.

### «Ya no veo mi clasificación»

Es intencionado, si su institución ha ocultado la clasificación a los estudiantes. El ajuste
está en [Lo que ven sus estudiantes](etablissement/parametres.md) — usted y su equipo siguen
viéndola.

### «No he recibido mis accesos»

Un acceso abierto no es un acceso recibido. Mire la columna de estado del acceso en su lista
de estudiantes: dice si ha salido y cuándo. Y la columna **Connected** dice si ya se ha
conectado — son dos preguntas distintas.

## Del lado de la campaña

### «La ronda de asignación se niega a arrancar»

El informe **nombra** a los estudiantes que bloquean, y la razón. Tres motivos impiden el
arranque:

| Mensaje | Qué hacer |
|---|---|
| **no student record** | No hay nada que colocar. |
| **no level track** | Asígnele una denominación de nivel (*Custom level*). Si su institución no las usa, cree una por nivel. |
| **no imported class rank** | Importe la clasificación antes de relanzar. La ronda no la fabrica. |

Un **expediente incompleto** no impide el arranque. Si la campaña está configurada en **Block
the assignment until everything is in hand**, el estudiante queda apartado y se le nombra en el
informe; con **Show it, assign anyway (recommended)**, se le asigna y se le señala. Los
estudiantes que han respondido «no deseo irme» nunca bloquean.

!!! tip "La ronda no es un gesto único"
    Corrija lo que bloquea y relánsela tantas veces como haga falta.

### «No puedo eliminar esta campaña»

Solo se elimina una campaña en **borrador**. Una campaña abierta ya lleva preferencias.

### «No puedo reabrir esta campaña»

Solo se reabre una campaña **terminada**. Si se reabre después de su hora de cierre,
**permanece abierta** hasta que usted la cierre: el cierre automático no vuelve a cerrarla.

### «Mi campaña se ha cerrado sola»

Su hora de cierre ha pasado: la campaña se cierra en el minuto que usted fijó, las preferencias
quedan congeladas y usted recibe el balance. Reábrala si era prematuro.

### «Mis contadores de plazas no dicen lo mismo que mi exportación»

Los contadores de plazas cubren las movilidades **salientes** — las que usted envía. Las plazas
que sus socios abren en su casa no inflan sus totales; el acuerdo las muestra aparte, en un
indicador de entrantes.

## Del lado del socio

### «No puedo recordárselo a este socio»

Un recordatorio cada veinticuatro horas. El botón se desactiva después, y su información
emergente indica la fecha del último recordatorio.

### «No puedo nominar a este estudiante en este acuerdo»

Dos causas. **No hay ningún contacto en este socio**: "No contact for this partner — add one
to be able to nominate." Añada un contacto en su ficha. **El estudiante ya está nominado**:
solo se puede nominar una asignación que aún no lo esté. Para empezar de nuevo, retire la
nominación y vuelva a asignarlo.

### «Este socio no aparece en mi campaña»

El grupo de destinos no lo retiene: compruebe los tipos de acuerdo, los periodos, el nivel, el
año académico, el tipo de movilidad y los filtros de institución de la campaña, y que el
acuerdo esté activo. Compruebe también que no esté archivado ni oculto.

### «No puedo rechazar esta nominación»

Un rechazo exige un motivo. Se transmitirá a la institución que le nominó al estudiante.

## Del lado de accesos y permisos

### «Esta pantalla es de solo lectura»

Su rol le da el nivel **View** en esta sección. Un banner lo indica en la parte superior de la
pantalla. Su pantalla [Mis permisos](etablissement/parametres.md) le dice exactamente qué puede
hacer y sobre quién.

### «Este estudiante está fuera de mi perímetro»

Su rol se limita a un ámbito de actividad, una dirección, un campus o unas promociones que no lo
cubren. No es una avería: es el perímetro definido por su administrador.

### «Parte de mi selección no se ha procesado»

Su acción afectaba a filas fuera de su perímetro. Se apartan, y la pantalla le dice cuántas.

### «No puedo conectarme con mi cuenta de la institución»

El inicio de sesión único verifica **quién es usted**; no decide que tenga derecho a entrar.
Su cuenta debe existir previamente en AroundLink. Véase
[Quién aporta qué](plateforme/sso-microsoft.md).

## Del lado de los documentos

### «No puedo guardar este resultado de idioma»

Un resultado exige siempre un justificante. Cuando lo introduce el propio estudiante, la fecha
del examen también es obligatoria.

### «Me piden un motivo para modificar el contrato de estudios»

Todo componente añadido o retirado tras la validación exige una justificación. Es una
exigencia del contrato, no un ajuste.
