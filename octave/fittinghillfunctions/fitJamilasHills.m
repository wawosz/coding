clear all;

conc = [1e-9; 1; 5; 10; 15; 20; 33; 50];
mu = [11.6; 26.75; 74.39; 121.03; 140.85; 444.6; 743.94; 872.84];
Mu = mu - mu(1);
st = [1; 5.77; 4.13; 4.68; 6.78; 54.02; 47.28; 151.62];

muMg = [11.6; 84.72; 175.41; 248.28; 476.26; 837.07; 1148.89; 1432.34];
MuMg = muMg - muMg(1);
stMg = [1; 15.46; 23.56; 46.94; 99.52; 141.97; 328.35; 428.54];

muEdta = [11.6; 15.65; 49.35; 63.78; 59.35; 81.75; 440.72; 387.23];
MuEdta = muEdta - muEdta(1);
stEdta = [0.26; 1.83; 6.57; 20.6; 24.01; 18.25; 37.57; 37.72];

muPeg4 = [4.78; 8.37; 18.20; 34.69; 46.14; 47.86; 441.47; 393.99];
MuPeg4 = muPeg4 - muPeg4(1);
stPeg4 = [0.54; 0.54; 2.88; 4.49; 9.88; 4.49; 80.90; 72.26];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
hCoef = 4;

km = fitHill(conc, Mu, ones(length(mu), 1), hCoef);
kmMg = fitHill(conc, MuMg, ones(length(mu), 1), hCoef);
kmEdta = fitHill(conc, MuEdta, ones(length(mu), 1), hCoef);
kmPeg4 = fitHill(conc, MuPeg4, ones(length(mu), 1), hCoef);

% km = ftHill(conc, mu, st, hCoef);
% kmMg = fitHill(conc, muMg, stMg, hCoef);

thrConc = 0.0:0.0001:(1.1 * max(conc));
thr = km(2) * 1./(1 + (km(1)./thrConc).^km(3));
thrMg = kmMg(2) * 1./(1 + (kmMg(1)./thrConc).^kmMg(3));
thrEdta = kmEdta(2) * 1./(1 + (kmEdta(1)./thrConc).^kmEdta(3));
thrPeg4 = kmPeg4(2) * 1./(1 + (kmPeg4(1)./thrConc).^kmPeg4(3));

close all;

%, zeros(1, length(mu))

figure;
hold on;
errorbar(conc, Mu, zeros(1, length(mu)), st, 'o', 'color', [0.2, 0.6, 0.4], 'MarkerFaceColor', [0.2, 0.6, 0.4], 'LineWidth', 2);
plot(thrConc, thr, 'color', [0.2, 0.6, 0.4], 'LineWidth', 2);
errorbar(conc, MuMg, zeros(1, length(mu)), stMg, 'o', 'color', [0.9, 0.4, 0], 'MarkerFaceColor', [0.9, 0.4, 0], 'LineWidth', 2);
plot(thrConc, thrMg, 'color', [0.9, 0.4, 0], 'LineWidth', 2);
errorbar(conc, MuEdta, zeros(1, length(mu)), stEdta, 'o', 'color', [1, 0.2, 0.2], 'MarkerFaceColor', [1, 0.2, 0.2], 'LineWidth', 2);
plot(thrConc, thrEdta, 'color', [1, 0.2, 0.2], 'LineWidth', 2);
errorbar(conc, MuPeg4, zeros(1, length(mu)), stPeg4, 'o', 'color', [0.2, 0.2, 1], 'MarkerFaceColor', [0.2, 0.2, 1], 'LineWidth', 2);
plot(thrConc, thrPeg4, 'color', [0.2, 0.2, 1], 'LineWidth', 2);
hold off;

%axis([0.0 0.6 0 2000]);
xlabel('[FITC-PEG_4-cRGD_2] (\mumol L^{-1})');
ylabel('Fluorescence (A.U.)');
legend('Untreated', '', '20 \mumol L^{-1} Mn^{2+}', '', '20 \mumol L^{-1} EDTA', '', '50 \mumol L^{-1} PEG_4-cRGD_2', '', 'Location', 'northwest');

set(gca, 'YTick', [0 500 1000 1500 2000]);