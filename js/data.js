
const profiles = [
  { id: 1, name: "Ana", skills: ["HTML", "CSS"], projects: [] }
];

export const db = {
  getProfiles: () => profiles,
  addProfile: (profile) => profiles.push(profile),
  getProfileById: (id) => profiles.find(p => p.id === id),
};
