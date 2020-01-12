% PLOTTING cRGD2 biodistribution

% data
organs = {'blood','lungs','skin','fat','liver','kidney (cortex)',...
    'kidney (medulla)','spleen','pancreas','intestines','aorta',...
    'heart (infarct)','heart (normal)','eye'};
cRGD2_mean = [0.5640 2.9540 2.0066 0.01 1.49872 11.08024 3.65862...
    2.24877 0.5971 4.61878 1.50839 4.09656 0.9673 1.28];
cRGD2_err = [0.05 0.43 0.29 0.007 0.4 2.2 0.4 0.33 0.14 0.24 0.15 0.39 0.12 0.07];

% ploting data
figure;
hold on
bar(cRGD2_mean,'k');
errorbar(cRGD2_mean,cRGD2_err,'k.','LineWidth',2);
set(gca,'fontsize', 16);
set(gca,'Xtick',1:14);
set(gca,'XTickLabelRotation',45);
set(gca,'XTickLabel',organs);
grid on;
grid minor;
title('^{64}Cu-PEG_4-cRGD_2 BIODISTRIBUTION');
xlabel('Time (s)');
ylabel('Radioactivity (%I.D./g)');
legend('Cu-64-PEG4-cRGD2');
hold off

% END OF FILE