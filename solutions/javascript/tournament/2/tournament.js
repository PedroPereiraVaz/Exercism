//
// This is only a SKELETON file for the 'Tournament' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

export const tournamentTally = (data) => {
  const INITIAL_STATS = { MP: 0, W: 0, D: 0, L: 0, P: 0 };
  const classification = {};
  const HEADER = "Team                           | MP |  W |  D |  L |  P";

  if (!data || data.trim() === "") return HEADER;

  const matches = data.split("\n");

  for (const match of matches) {
    const [team1, team2, result] = match.split(";");

    classification[team1] ??= { ...INITIAL_STATS };
    classification[team2] ??= { ...INITIAL_STATS };

    classification[team1].MP += 1;
    classification[team2].MP += 1;

    if (result === "win") {
      classification[team1].W += 1;
      classification[team1].P += 3;
      classification[team2].L += 1;
    } else if (result === "loss") {
      classification[team2].W += 1;
      classification[team2].P += 3;
      classification[team1].L += 1;
    } else if (result === "draw") {
      classification[team1].D += 1;
      classification[team1].P += 1;
      classification[team2].D += 1;
      classification[team2].P += 1;
    }
  }

  const finalRanking = Object.entries(classification).map(([name, stats]) => ({name: name,...stats,}));

  finalRanking.sort((a, b) => {
    if (a.P !== b.P) return b.P - a.P;
    return a.name.localeCompare(b.name);
  });

  const tableRows = finalRanking.map((team) => {
    const { name, MP, W, D, L, P } = team;
    return `${name.padEnd(31)}|  ${MP} |  ${W} |  ${D} |  ${L} | ${String(P).padStart(2)}`;
  });

  return [HEADER, ...tableRows].join("\n");
};
