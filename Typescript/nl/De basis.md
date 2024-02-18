Welkom op de eerste pagina van de handleiding. Als dit je eerste kennismaking is met TypeScript, wil je misschien beginnen met een van de '[Getting Started](https://www.typescriptlang.org/docs/handbook/intro.html#get-started)' handleidingen.

Elke waarde in JavaScript vertoont een reeks gedragingen die je kunt observeren bij het uitvoeren van verschillende bewerkingen. Dat klinkt abstract, maar als snel voorbeeld, overweeg enkele bewerkingen die we kunnen uitvoeren op een variabele met de naam `message`.

```typescript
// Toegang tot de eigenschap 'toLowerCase' op 'message' en vervolgens het aanroepen ervan
message.toLowerCase();
// Aanroepen van 'message' zelf
message();
```

Als we dit ontleden, wordt de eerste uitvoerbare regel code een eigenschap genaamd `toLowerCase` aan die op `message` en roept deze vervolgens aan. De tweede probeert `message` rechtstreeks aan te roepen.

Maar als we de waarde van `message` niet weten - en dat komt vaak voor - kunnen we niet betrouwbaar zeggen welke resultaten we krijgen bij het proberen uit te voeren van een van deze codes. Het gedrag van elke bewerking hangt volledig af van de waarde die we aanvankelijk hadden.

- Is `message` aanroepbaar?
- Heeft het een eigenschap genaamd `toLowerCase`?
- Als dat het geval is, is `toLowerCase` zelfs aanroepbaar?
- Als beide waarden aanroepbaar zijn, wat geven ze dan terug?

De antwoorden op deze vragen zijn meestal dingen die we in ons hoofd houden wanneer we JavaScript schrijven, en we moeten hopen dat we alle details correct hebben.

Laten we zeggen dat `message` op de volgende manier is gedefinieerd.

```typescript
const message = "Hallo wereld!";
```

Zoals je waarschijnlijk kunt raden, als we `message.toLowerCase()` proberen uit te voeren, krijgen we dezelfde string maar dan in kleine letters.

Hoe zit het met die tweede regel code? Als je bekend bent met JavaScript, weet je dat dit mislukt met een uitzondering:

```typescript
TypeError: message is geen functie
```

Het zou geweldig zijn als we fouten zoals deze konden vermijden.

Wanneer we onze code uitvoeren, kiest onze JavaScript-runtime op basis van het _type_ van de waarde hoe het moet handelen - welke gedragingen en mogelijkheden het heeft. Dat is een deel van wat die `TypeError` aanduidt - het zegt dat de string "Hello World!" niet kan worden aangeroepen als een functie.

Voor sommige waarden, zoals de primitieven `string` en `number`, kunnen we hun type tijdens runtime identificeren met de operator `typeof`. Maar voor andere dingen zoals functies is er geen overeenkomstig runtimemechanisme om hun typen te identificeren. Overweeg bijvoorbeeld deze functie:

```typescript
function fn(x) {
  return x.flip();
}
```

We kunnen _observeren_ door de code te lezen dat deze functie alleen zal werken als deze wordt gegeven aan een object met een aanroepbare eigenschap `flip`, maar JavaScript geeft deze informatie niet op een manier die we kunnen controleren terwijl de code wordt uitgevoerd. De enige manier om erachter te komen wat `fn` doet met een bepaalde waarde is om het aan te roepen en te zien wat er gebeurt. Dit soort gedrag maakt het moeilijk om te voorspellen wat de code zal doen voordat deze wordt uitgevoerd, wat betekent dat het moeilijker is om te weten wat je code gaat doen terwijl je deze schrijft.

Op deze manier gezien is een _type_ het concept van beschrijven welke waarden kunnen worden doorgegeven aan `fn` en welke een fout veroorzaken. JavaScript biedt alleen echt _dynamische_ typering - het uitvoeren van de code om te zien wat er gebeurt.

De alternatieve aanpak is het gebruik van een _statisch_ typesysteem om voorspellingen te doen over wat de code _verwacht_ te doen _voordat_ deze wordt uitgevoerd.

## [Statische typecontrole](https://www.typescriptlang.org/docs/handbook/2/basic-types.html#static-type-checking)

Denk terug aan die `TypeError` die we eerder kregen bij het proberen aan te roepen van een `string` als een functie. De meeste mensen houden er niet van om fouten te krijgen bij het uitvoeren van hun code - die worden als bugs beschouwd! En wanneer we nieuwe code schrijven, proberen we ons best te doen om geen nieuwe bugs te introduceren.

Als we gewoon een beetje code toevoegen, ons bestand opslaan, de code opnieuw uitvoeren en meteen de fout zien, kunnen we het probleem misschien snel isoleren; maar dat is niet altijd het geval. We hebben de functie misschien niet grondig genoeg getest, dus het kan zijn dat we nooit echt een potentieel fout zouden tegenkomen die wordt veroorzaakt! Of als we geluk hadden om de fout te zien, hebben we misschien grote refactoren gedaan en veel verschillende code toegevoegd die we gedwongen zijn door te spitten.

Idealiter zouden we een hulpmiddel willen hebben dat ons helpt deze bugs te vinden _voordat_ onze code wordt uitgevoerd. Dat is wat een statische typechecker zoals TypeScript doet. _Statische typesystemen_ beschrijven de vormen en gedragingen van wat onze waarden zullen zijn wanneer we onze programma's uitvoeren. Een typechecker zoals TypeScript gebruikt die informatie en vertelt ons wanneer dingen missch

ien niet kloppen.

Laten we eens kijken naar een voorbeeld om te zien hoe statische typecontrole werkt in TypeScript. Stel je voor dat we een functie hebben die twee getallen toevoegt:

```typescript
function add(x, y) {
  return x + y;
}
```

Dit lijkt op een eenvoudige functie die twee getallen bij elkaar optelt, maar het heeft een potentieel probleem. Wat als iemand deze functie aanroept met twee strings? In JavaScript zou de uitvoer een string zijn die de twee waarden gewoon aan elkaar plakt:

```typescript
const result = add("Hello", "World");
console.log(result); // "HelloWorld"
```

Dit kan een onbedoeld gedrag zijn. Misschien willen we echt dat `add` alleen wordt gebruikt met getallen, en als iemand het met iets anders probeert, willen we dat de code niet eens compileert of, als het wordt uitgevoerd, een duidelijke fout oplevert.

Hier komt TypeScript binnen. Als we onze `add`-functie in TypeScript schrijven, kunnen we de _types_ van `x` en `y` specificeren:

```typescript
function add(x: number, y: number): number {
  return x + y;
}
```

Deze notatie `x: number` betekent dat we verwachten dat `x` een getal is. Door deze informatie te geven, kan TypeScript ons helpen fouten te voorkomen. Als we proberen `add` op te roepen met strings, geeft TypeScript ons een foutmelding:

```typescript
const result = add("Hello", "World"); // Fout: Argument van het type 'string' kan niet worden toegewezen aan het parameter type 'number'.
```

Dit is een eenvoudig voorbeeld, maar het illustreert het principe van statische typecontrole. Door het type van onze waarden te specificeren, kunnen we fouten identificeren voordat we onze code uitvoeren.

## [Type-annotaties](https://www.typescriptlang.org/docs/handbook/2/basic-types.html#type-annotations)

In het vorige voorbeeld hebben we type-annotaties gebruikt om het verwachte type van de parameters en het retourtype van de functie aan te geven. Type-annotaties in TypeScript worden geschreven met een dubbele punt (`:`).

Hier zijn enkele basisprincipes van type-annotaties:

### Variabelen

```typescript
let age: number = 25;
let name: string = "John";
let isStudent: boolean = true;
```

Hier worden variabelen `age`, `name` en `isStudent` geannoteerd met respectievelijk de typen `number`, `string` en `boolean`.

### Functies

```typescript
function greet(person: string): string {
  return "Hello, " + person;
}
```

De functie `greet` neemt een argument `person` van het type `string` en retourneert een waarde van het type `string`.

### Arrays

```typescript
let numbers: number[] = [1, 2, 3, 4];
let names: string[] = ["Alice", "Bob", "Charlie"];
```

De variabelen `numbers` en `names` worden geannoteerd als arrays van respectievelijk getallen en strings.

### Objecten

```typescript
let person: { name: string; age: number } = {
  name: "John",
  age: 30,
};
```

De variabele `person` is geannoteerd als een object met eigenschappen `name` van het type `string` en `age` van het type `number`.

Dit zijn slechts enkele basisvoorbeelden. TypeScript biedt een rijk scala aan typemogelijkheden om complexere structuren en gedragingen van je code te beschrijven.

## [Inferentie van typen](https://www.typescriptlang.org/docs/handbook/2/basic-types.html#type-inference)

In TypeScript hoef je niet altijd expliciet typen aan te geven. TypeScript kan veel typen _afleiden_ op basis van de manier waarop je code is geschreven. Dit staat bekend als _inferentie van typen_. Hier zijn enkele voorbeelden:

### Variabelen

```typescript
let age = 25; // TypeScript kan afleiden dat 'age' een 'number' is.
let name = "John"; // TypeScript kan afleiden dat 'name' een 'string' is.
let isStudent = true; // TypeScript kan afleiden dat 'isStudent' een 'boolean' is.
```

### Functies

```typescript
function greet(person: string) {
  return "Hello, " + person;
}
```

In dit voorbeeld hoeven we het retourtype niet expliciet op te geven, omdat TypeScript het kan afleiden op basis van de string die wordt samengevoegd.

### Arrays

```typescript
let numbers = [1, 2, 3, 4]; // TypeScript kan afleiden dat 'numbers' een array van getallen is.
let names = ["Alice", "Bob", "Charlie"]; // TypeScript kan afleiden dat 'names' een array van strings is.
```

### Objecten

```typescript
let person = {
  name: "John",
  age: 30,
}; // TypeScript kan afleiden dat 'person' een object is met eigenschappen 'name' (string) en 'age' (number).
```

Inferentie van typen kan het gemakkelijker maken om TypeScript te gebruiken zonder de noodzaak van uitgebreide type-annotaties, maar het is nog steeds een goed idee om expliciet typen aan te geven in veel situaties om de leesbaarheid van de code te verbeteren en fouten te voorkomen.

## [Union Types](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#union-types)

Tot nu toe hebben we gezien hoe we specifieke typen kunnen aangeven, zoals `number`, `string`, `boolean`, enz. Maar wat als een waarde meer dan één type kan hebben? Hier komen _union types_ van pas.

Stel je bijvoorbeeld voor dat we een functie hebben die ofwel een getal ofwel een string accepteert:

```typescript
function printId(id: number | string) {
  console.log("ID is:", id);
}
```

De `id`-parameter is hier van het type `number | string`, wat betekent dat het een getal _of_ een string kan zijn. Als we deze functie aanroepen met een getal of een string, is alles goed:

```typescript
printId(101); // ID is: 101
printId("abc"); // ID is: abc
```

Union types kunnen ook hand **TypeError: Expected 2 arguments, but got 1**

```typescript
function add(x: number, y: number): number {
  return x + y;
}

// Correcte oproepen
const result1 = add(5, 3);
console.log(result1); // 8

const result2 = add(10, -2);
console.log(result2); // 8

// Foutieve oproep, omdat we slechts één argument doorgeven
const result3 = add(5); // Fout: Verwacht 2 argumenten, maar kreeg er 1.
```

In dit voorbeeld is `add` een functie die twee getallen verwacht en hun som retourneert. Door de type-annotaties `x: number` en `y: number` weten we dat beide parameters getallen moeten zijn. Als we de functie correct oproepen met twee getallen, krijgen we het verwachte resultaat. Echter, als we de functie oproepen met slechts één argument, krijgen we een foutmelding van TypeScript omdat het aantal argumenten niet overeenkomt met wat de functie verwacht.

**TypeError: Argument of type 'string' is not assignable to parameter of type 'number'**

```typescript
function greet(person: string): string {
  return "Hello, " + person;
}

// Correcte oproep
const greeting1 = greet("Alice");
console.log(greeting1); // Hello, Alice

// Foutieve oproep, omdat we een string doorgeven aan een functie die een persoon van het type 'string' verwacht
const greeting2 = greet(42); // Fout: Argument van het type 'number' kan niet worden toegewezen aan het parameter type 'string'.
```

In dit voorbeeld verwacht de functie `greet` een string als argument. Als we de functie correct oproepen met een string, krijgen we het gewenste resultaat. Echter, als we de functie oproepen met een getal, krijgen we een foutmelding van TypeScript omdat het opgegeven type niet overeenkomt met het verwachte type.

**TypeError: Property 'length' does not exist on type 'number'**

```typescript
function getLength(value: string | number): number {
  return value.length;
}

// Foutieve oproep, omdat TypeScript niet zeker weet of 'value' een string is
const length = getLength(42); // Fout: Property 'length' does not exist on type 'number'.
```

In dit voorbeeld is `getLength` een functie die de lengte van een string of een getal retourneert. Echter, TypeScript kan niet zeker weten of `value` een string is, dus het geeft een foutmelding wanneer we proberen de `length` eigenschap te gebruiken op `value` van het type `string | number`.

**Correct gebruik van Union Types**

```typescript
function getLength(value: string | number): number {
  if (typeof value === "string") {
    return value.length;
  } else {
    return value.toString().length;
  }
}

// Correcte oproepen
const length1 = getLength("Hello"); // lengte van de string
console.log(length1); // 5

const length2 = getLength(123); // lengte van de getal als string
console.log(length2); // 3
```

In dit geval gebruiken we een conditie (`typeof value === "string"`) om te controleren of `value` een string is voordat we de `length` eigenschap gebruiken. Als het geen string is, converteren we het naar een string met `toString()` voordat we de lengte berekenen. Dit voorkomt de TypeScript-fout omdat we nu zeker weten dat we de `length` eigenschap alleen op een string gebruiken.

**Correct gebruik van Optionele Parameters**

```typescript
function greet(person: string, greeting?: string): string {
  if (greeting) {
    return greeting + ", " + person;
  } else {
    return "Hello, " + person;
  }
}

// Correcte oproepen
const greeting1 = greet("Alice");
console.log(greeting1); // Hello, Alice

const greeting2 = greet("Bob", "Good morning");
console.log(greeting2); // Good morning, Bob
```

In dit voorbeeld hebben we een optionele parameter `greeting` toegevoegd aan de functie `greet`. Het vraagteken (`?`) geeft aan dat de parameter niet vereist is bij het aanroepen van de functie. Als de parameter aanwezig is, wordt de begroeting samengesteld met de opgegeven begroeting, anders wordt de standaardbegroeting gebruikt.

**Correct gebruik van Standaardwaarden voor Parameters**

```typescript
function greet(person: string, greeting: string = "Hello"): string {
  return greeting + ", " + person;
}

// Correcte oproepen
const greeting1 = greet("Alice");
console.log(greeting1); // Hello, Alice

const greeting2 = greet("Bob", "Good morning");
console.log(greeting2); // Good morning, Bob
```

Een andere manier om optionele parameters te hanteren, is door standaardwaarden aan parameters toe te wijzen. In dit geval heeft de `greeting`-parameter een standaardwaarde van "Hello". Als de parameter niet wordt opgegeven bij het aanroepen van de functie, wordt automatisch de standaardwaarde gebruikt.

**Correct gebruik van Rest Parameters**

```typescript
function sum(...numbers: number[]): number {
  return numbers.reduce((total, num) => total + num, 0);
}

// Correcte oproepen
const result1 = sum(1, 2, 3);
console.log(result1); // 6

const result2 = sum(4, 5, 6, 7);
console.log(result2); // 22
```

De functie `sum` accepteert een willekeurig aantal getallen als argumenten met behulp van de rest parameters (`...numbers: number[]`). Hierdoor kunnen we een variabel aantal getallen doorgeven aan de functie, en ze worden behandeld als een array met de naam `numbers`. De functie gebruikt vervolgens de `reduce`-methode om de som van alle getallen te berekenen.

**Correct gebruik van Generics**

Generics stellen je in staat om functies, klassen en interfaces te schrijven waarbij het type van bepaalde gegevens wordt uitgesteld tot het moment van gebruik. Dit vergroot de herbruikbaarheid van code en zorgt voor sterke typen. Hier zijn enkele voorbeelden:

```typescript
// Generieke functie die een array omkeert
function reverseArray<T>(array: T[]): T[] {
  return array.reverse();
}

const numbers = [1, 2, 3, 4, 5];
const reversedNumbers = reverseArray(numbers);
console.log(reversedNumbers); // [5, 4, 3, 2, 1]

const words = ["apple", "banana", "orange"];
const reversedWords = reverseArray(words);
console.log(reversedWords); // ["orange", "banana", "apple"]
```

In dit voorbeeld hebben we een generieke functie `reverseArray` gemaakt die werkt met een array van elk type `T`. De functie keert de elementen van de array om en retourneert de omgekeerde array.

```typescript
// Generieke klasse voor een eenvoudige stapel (stack)
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }

  pop(): T | undefined {
    return this.items.pop();
  }
}

// Gebruik van de generieke klasse
const numberStack = new Stack<number>();
numberStack.push(1);
numberStack.push(2);
numberStack.push(3);

console.log(numberStack.pop()); // 3
console.log(numberStack.pop()); // 2
```

Hier hebben we een generieke klasse `Stack` gemaakt, die werkt met een willekeurig type `T`. De klasse heeft methoden om een item toe te voegen aan de stapel (`push`) en om een item van de stapel te verwijderen (`pop`).

Generics bieden flexibiliteit en herbruikbaarheid in TypeScript, en ze kunnen worden toegepast op verschillende aspecten van je code, zoals functies, klassen en interfaces. 

**Asynchrone Programmeerfuncties in TypeScript**

In TypeScript kun je asynchrone programmeerfuncties maken met behulp van `async` en `await`. Dit maakt het mogelijk om code te schrijven die non-blocking is en efficiënt omgaat met taken zoals het ophalen van gegevens van een externe bron, wachten op gebruikersinvoer, of het uitvoeren van andere taken die tijd kunnen kosten. Hier is een eenvoudig voorbeeld:

```typescript
// Een asynchrone functie die na een vertraging een bericht logt
async function delayedMessage(message: string, delay: number): Promise<void> {
  return new Promise<void>((resolve) => {
    setTimeout(() => {
      console.log(message);
      resolve();
    }, delay);
  });
}

// Gebruik van de asynchrone functie met await
async function main() {
  console.log("Start van het programma");

  await delayedMessage("Dit bericht verschijnt na 2 seconden", 2000);
  await delayedMessage("En dit bericht verschijnt nog eens na 1 seconde", 1000);

  console.log("Einde van het programma");
}

// Roep de hoofdfunctie aan
main();
```

In dit voorbeeld gebruiken we de `async`-sleutelwoord om de `delayedMessage`-functie asynchroon te maken. Binnen de functie gebruiken we `await` om te wachten op de voltooiing van de vertraagde taak (in dit geval, een `Promise` die na een bepaalde vertraging wordt opgelost).

Merk op dat de `main`-functie ook als asynchroon is gemarkeerd en dat we deze aanroepen met `await`. Dit zorgt ervoor dat het programma wacht op de voltooiing van elke taak voordat het doorgaat.

Asynchrone programmeertechnieken zijn vooral handig bij het werken met I/O-operaties, zoals het ophalen van gegevens van een server of het lezen van bestanden.

**Fetch API in TypeScript voor het ophalen van gegevens van een server**

In TypeScript kun je de Fetch API gebruiken om gegevens van een server op te halen. Hier is een eenvoudig voorbeeld:

```typescript
// Een asynchrone functie die gegevens ophaalt van een server
async function fetchData(url: string): Promise<void> {
  try {
    // Gebruik fetch om gegevens op te halen van de opgegeven URL
    const response = await fetch(url);

    // Controleer of het verzoek succesvol was (status 200-299)
    if (!response.ok) {
      throw new Error(`Fout bij het ophalen van gegevens: ${response.status}`);
    }

    // Converteer de ontvangen gegevens naar JSON-formaat
    const data = await response.json();

    // Doe iets met de opgehaalde gegevens (bijv. loggen)
    console.log("Opgelhaalde gegevens:", data);
  } catch (error) {
    console.error("Fout bij het ophalen van gegevens:", error.message);
  }
}

// Gebruik de fetchData-functie met een voorbeeld-URL
const exampleUrl = 'https://jsonplaceholder.typicode.com/todos/1';
fetchData(exampleUrl);
```

In dit voorbeeld hebben we een asynchrone functie `fetchData` gemaakt die een URL accepteert, gegevens ophaalt van die URL met behulp van `fetch`, en vervolgens de ontvangen gegevens logt. We gebruiken `await` om te wachten op de voltooiing van het fetch-verzoek en het omzetten van de respons naar JSON.

Merk op dat we ook een foutafhandeling hebben toegevoegd om eventuele problemen tijdens het ophalen van gegevens te behandelen. Dit is belangrijk, omdat het fetch-verzoek kan mislukken om verschillende redenen.

Je kunt de `fetchData`-functie aanroepen met de URL van de server die je wilt bevragen. In het voorbeeld gebruiken we een willekeurige JSONPlaceholder URL.

**Typescript: Asynchrone Functies en het Gebruik van Async/Await**

In TypeScript kun je asynchrone functies en `async/await` gebruiken om asynchrone code te schrijven die duidelijk en leesbaar is. Hier is een voorbeeld van hoe je dit kunt doen:

```typescript
// Een voorbeeld van een asynchrone functie met async/await
async function fetchData(url: string): Promise<void> {
  try {
    // Gebruik fetch om gegevens op te halen van de opgegeven URL
    const response = await fetch(url);

    // Controleer of het verzoek succesvol was (status 200-299)
    if (!response.ok) {
      throw new Error(`Fout bij het ophalen van gegevens: ${response.status}`);
    }

    // Converteer de ontvangen gegevens naar JSON-formaat
    const data = await response.json();

    // Doe iets met de opgehaalde gegevens (bijv. loggen)
    console.log("Opgelhaalde gegevens:", data);
  } catch (error) {
    console.error("Fout bij het ophalen van gegevens:", error.message);
  }
}

// Een voorbeeld van het aanroepen van de fetchData-functie
const exampleUrl = 'https://jsonplaceholder.typicode.com/todos/1';
fetchData(exampleUrl);
```

In dit voorbeeld hebben we de `fetchData`-functie aangepast om het `async`-sleutelwoord toe te voegen aan de functiedeclaratie. Hierdoor wordt de functie automatisch een asynchrone functie.

Het `await`-woord wordt gebruikt om te wachten op de voltooiing van asynchrone operaties, zoals het fetchen van gegevens of het uitvoeren van andere asynchrone functies. Dit maakt de code leesbaarder en lijkt meer op synchrone code, hoewel het nog steeds asynchroon is onder de motorkap.

Het gebruik van `try/catch` om fouten af ​​te handelen, is ook belangrijk om robuuste asynchrone code te schrijven. Hiermee kun je adequaat reageren op fouten die kunnen optreden tijdens het uitvoeren van de asynchrone operatie.

**Typescript: Promises en Callbacks**

In TypeScript kun je asynchrone code beheren met behulp van Promises en Callbacks. Promises bieden een gestructureerde manier om met asynchrone operaties om te gaan, terwijl Callbacks een meer traditionele benadering zijn. Hier zijn voorbeelden van beide:

1. **Promises:**

   ```typescript
   // Een voorbeeld van een functie die een Promise retourneert
   function fetchDataWithPromise(url: string): Promise<void> {
     return new Promise((resolve, reject) => {
       fetch(url)
         .then(response => {
           if (!response.ok) {
             throw new Error(`Fout bij het ophalen van gegevens: ${response.status}`);
           }
           return response.json();
         })
         .then(data => {
           console.log("Opgelhaalde gegevens (Promise):", data);
           resolve(); // De Promise wordt met succes opgelost
         })
         .catch(error => {
           console.error("Fout bij het ophalen van gegevens (Promise):", error.message);
           reject(error); // De Promise wordt afgewezen met de fout
         });
     });
   }

   // Een voorbeeld van het aanroepen van de fetchDataWithPromise-functie
   const promiseExampleUrl = 'https://jsonplaceholder.typicode.com/todos/1';
   fetchDataWithPromise(promiseExampleUrl)
     .then(() => console.log("Data met Promise opgehaald"))
     .catch(() => console.error("Fout bij het ophalen van gegevens met Promise"));
   ```

   In dit voorbeeld gebruiken we een Promise om het asynchrone gedrag van de `fetchDataWithPromise`-functie te beheren. Het `resolve`-gedeelte wordt aangeroepen wanneer de operatie met succes is voltooid, terwijl het `reject`-gedeelte wordt aangeroepen als er een fout optreedt.

2. **Callbacks:**

   ```typescript
   // Een voorbeeld van een functie met een callback-parameter
   function fetchDataWithCallback(url: string, callback: (data: any, error?: Error) => void): void {
     fetch(url)
       .then(response => {
         if (!response.ok) {
           throw new Error(`Fout bij het ophalen van gegevens: ${response.status}`);
         }
         return response.json();
       })
       .then(data => {
         console.log("Opgelhaalde gegevens (Callback):", data);
         callback(data); // Roep de callback aan met de opgehaalde gegevens
       })
       .catch(error => {
         console.error("Fout bij het ophalen van gegevens (Callback):", error.message);
         callback(null, error); // Roep de callback aan met een fout als die er is
       });
   }

   // Een voorbeeld van het aanroepen van de fetchDataWithCallback-functie
   const callbackExampleUrl = 'https://jsonplaceholder.typicode.com/todos/1';
   fetchDataWithCallback(callbackExampleUrl, (data, error) => {
     if (data) {
       console.log("Data met Callback opgehaald");
     } else {
       console.error("Fout bij het ophalen van gegevens met Callback", error);
     }
   });
   ```

   Hier gebruiken we een callback-functie om met het asynchrone resultaat om te gaan. De callback wordt aangeroepen met de opgehaalde gegevens als er geen fout is, anders wordt de fout meegegeven aan de callback.

Beide benaderingen hebben hun plaats, maar Promises worden vaak als moderner en gemakkelijker te begrijpen beschouwd. Het gebruik van Promises maakt ook het gebruik van `async/await` mogelijk, zoals eerder besproken.

**Typescript: Async/Await**

Async/Await is een syntactische suikerlaag boven op Promises en biedt een nog eenvoudigere manier om asynchrone code te schrijven. Hier is een voorbeeld van het gebruik van Async/Await in TypeScript:

```typescript
// Een voorbeeld van een asynchrone functie met Async/Await
async function fetchDataWithAsyncAwait(url: string): Promise<void> {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error(`Fout bij het ophalen van gegevens: ${response.status}`);
    }

    const data = await response.json();
    console.log("Opgelhaalde gegevens (Async/Await):", data);

    // De functie keert een Promise<void> terug, die automatisch wordt opgelost.
  } catch (error) {
    console.error("Fout bij het ophalen van gegevens (Async/Await):", error.message);

    // Als er een fout optreedt, wordt de Promise met de fout afgewezen.
    throw error;
  }
}

// Een voorbeeld van het aanroepen van de fetchDataWithAsyncAwait-functie
const asyncAwaitExampleUrl = 'https://jsonplaceholder.typicode.com/todos/1';

// Om deze functie aan te roepen, gebruiken we opnieuw async/await binnen een async context.
async function fetchDataExample() {
  try {
    await fetchDataWithAsyncAwait(asyncAwaitExampleUrl);
    console.log("Data met Async/Await opgehaald");
  } catch (error) {
    console.error("Fout bij het ophalen van gegevens met Async/Await", error);
  }
}

// Roep de fetchDataExample-functie aan
fetchDataExample();
```

In dit voorbeeld hebben we een asynchrone functie `fetchDataWithAsyncAwait` gemaakt met het `async`-sleutelwoord. Binnen deze functie gebruiken we `await` om op de resultaten van asynchrone operaties te wachten. Dit maakt de code leesbaarder en lijkt meer op synchrone code.

Bovendien hebben we een aparte functie `fetchDataExample` gemaakt om de `fetchDataWithAsyncAwait`-functie aan te roepen. Aangezien `fetchDataExample` ook asynchroon is, kunnen we `await` gebruiken om op het resultaat van `fetchDataWithAsyncAwait` te wachten.

Async/Await is vaak de voorkeursbenadering voor asynchrone code in moderne TypeScript- en JavaScript-toepassingen vanwege de verbeterde leesbaarheid en onderhoudsgemak.

