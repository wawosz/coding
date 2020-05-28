% PLOTTING Time Activity Curves of dynamic PET data with cRGD2

% importing XLS file
filename = 'Rat1817_1wkMI.xlsx';
data = xlsread(filename);

% defining column vectors
Time = data(1:60,1);
LV_Mean = data(1:60,2);
LV_Error = data(1:60,3);
Lung_Mean = data(1:60,4);
Lung_Error = data(1:60,5);
Liver_Mean = data(1:60,6);
Liver_Error = data(1:60,7);
Spleen_Mean = data(1:60,8);
Spleen_Error = data(1:60,9);
Bladder_Mean = data(1:60,10);
Bladder_Error = data(1:60,11);
RV_Mean = data(1:60,12);
RV_Error = data(1:60,13);
Jugular_Mean = data(1:60,14);
Jugular_Error = data(1:60,15);
Aorta_Mean = data(1:60,16);
Aorta_Error = data(1:60,17);
KidneyMed_Mean = data(1:60,18);
KidneyMed_Error = data(1:60,19);
KidneyCor_Mean =  data(1:60,20);
KidneyCor_Error = data(1:60,21);

% ploting data
figure;
hold on
plot(Time, LV_Mean, 'k-o', 'LineWidth', 1.5, 'MarkerFaceColor', 'k');
plot(Time, Aorta_Mean, 'k-x', 'LineWidth', 1.5);
set(gca,'fontsize', 16);
grid on;
grid minor;
title('BLOOD CLEARANCE');
xlabel('Time (s)');
ylabel('Radioactivity (%I.D./g)');
legend('Venous blood', 'Aortic blood');
hold off

figure;
hold on
plot(Time, Bladder_Mean, 'k-', 'LineWidth', 1.5);
plot(Time, KidneyMed_Mean, 'k-x', 'LineWidth', 1.5);
plot(Time, KidneyCor_Mean, 'k-o', 'LineWidth', 1.5, 'MarkerFaceColor','k');
plot(Time, Liver_Mean, 'k-+', 'LineWidth', 1.5);
set(gca,'fontsize', 16);
grid on
grid minor
title('TIME ACTIVITY CURVES (Selected Organs)');
xlabel('Time (s)');
ylabel('Radioactivity (%I.D./g)');
legend('Bladder', 'Kidney (medulla)', 'Kidney (cortex)', 'Liver',...
    'Location', 'east', 'FontSize', 12);
hold off

% END OF FILE