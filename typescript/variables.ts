// 3 atomic variable types
let player_name: string = "Maria";
let player_age: number = 19;
let player_active: boolean = true;

// lists
let players_list: string[] = ["Maria", "Abir", "John"];
let players_age: number[] = [19, 23, 25];

// tuples ( values inside are changable)
let player_info: [string, number]
player_info = ["Abir", 23]
console.log(player_info)
player_info = ["Maria", 19]

//functions
function generate_biodata(name: string, age: number): string {
    return `Player ${name} is ${age} years old`
}

console.log(generate_biodata("Abir", 23))

//optional parameters and returns nothing
function create_user(name: string, age?: number): void {
    if (age) {
        console.log(`User created with the name: ${name} and age: ${age}`)
    } else {
        console.log(`User created with the name: ${name}`)
    }
}

create_user("Maria")
create_user("Abir", 23)

/*

Write a function named runTestCase that meets these requirements:
    1. Takes a testName (string).
    2. Takes an attempts count (number).
    3. Takes an optional isCritical flag (boolean).
Returns a string.

*/

function runTestCase(testName: string, count: number, isCritical?: boolean): string {
    let output: string;
    if (isCritical) {
        output = `Critical Test Set created with the name: ${testName} and this set contains ${count} tests in it`;
    } else {
        output = `Test Set created with the name: ${testName} and this set contains ${count} tests in it`;
    }
    return output
}

console.log(runTestCase("MariaTest", 10, true))
console.log(runTestCase("AbirTest", 3))