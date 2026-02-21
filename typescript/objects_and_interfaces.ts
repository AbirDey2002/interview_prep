interface Developer {
    name: String;
    favouriteLanguage: string;
    experienceNumber: number;
    githubUrl?: string;
    readonly id: number;
}

let abir: Developer = {
    id: 101,
    name: "Abir",
    favouriteLanguage: "English",
    experienceNumber: 1.5,
    githubUrl: "https://github.com/AbirDey2002"
}

console.log(abir.id)