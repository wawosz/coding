% PLOTTING HPLC chromatograms with cRGD2

% importing XLS files
filename = 'cRGD2_metabolism.xlsx';
data_cRGD2 = xlsread(filename);

% defining column vectors
Time = data_cRGD2(1:1799,1);
cRGD2_Peak = data_cRGD2(1:1799,2);
Cu64_Peak = data_cRGD2(1:1799,3);
cRGD2_Urine_Peak = data_cRGD2(1:1799,4);
cRGD2_Feces_Peak = data_cRGD2(1:1799,5);

% ploting data
figure;
fig1 = subplot(2,1,1);
plot(fig1, Time, cRGD2_Peak, 'k-', 'LineWidth', 1.5);
set(gca,'fontsize', 14);
grid on;
grid minor;
ylim(fig1,[0 1000]);
xlabel(fig1, 'Time (min)');
ylabel(fig1, 'Radioactivity (CPM)');
legend(fig1, '^{64}Cu-PEG_{4}-cRGD_{2} in acetate buffer');

fig2 = subplot(2,1,2);
plot(fig2, Time, Cu64_Peak, 'k-', 'LineWidth', 1.5);
set(gca,'fontsize', 14);
grid on;
grid minor;
ylim(fig2,[0 1000]);
xlabel(fig2, 'Time (min)');
ylabel(fig2, 'Radioactivity (CPM)');
legend(fig2, '^{64}Cu acetate');

figure;
fig1 = subplot(2,1,1);
plot(fig1, Time, cRGD2_Urine_Peak, 'k-', 'LineWidth', 1.5);
set(gca,'fontsize', 14);
grid on;
grid minor;
ylim(fig1,[0 300]);
xlabel(fig1, 'Time (min)');
ylabel(fig1, 'Radioactivity (CPM)');
legend(fig1, '^{64}Cu-PEG_{4}-cRGD_{2} in urine');

fig2 = subplot(2,1,2);
plot(fig2, Time, cRGD2_Feces_Peak, 'k-', 'LineWidth', 1.5);
set(gca,'fontsize', 14);
grid on;
grid minor;
ylim(fig2,[0 300]);
xlabel(fig2, 'Time (min)');
ylabel(fig2, 'Radioactivity (CPM)');
legend(fig2, '^{64}Cu-PEG_{4}-cRGD_{2} in feces');

% END OF FILE