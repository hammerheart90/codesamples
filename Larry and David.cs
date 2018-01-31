using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            double earlDeposit = 0;
            double larryDeposit = 0;
            for (int i = 1; i <= 33; i++)
            {
                larryDeposit = i * 5000;
            }

            for (int i = 1; i <= 15; i++)
            {
                earlDeposit = i * 5000;
            }

            double balanceEarl = 0;
            for (int i = 1; i <= 15; i++)
            {
                balanceEarl = balanceEarl + (5000 + (balanceEarl * 0.04));
            }

            for (int i = 1; i <= 33; i++)
            {
                balanceEarl += (balanceEarl * 0.04);
            }

            double balanceLarry = 0;
            for (int i = 1; i <= 33; i++)
            {
                balanceLarry += (balanceLarry * 0.04) + 5000;
            }

            txtDepositEarl.Text = earlDeposit.ToString("C2");
            txtDepositLarry.Text = larryDeposit.ToString("C2");
            txtAmountEarl.Text = balanceEarl.ToString("C2");
            txtAmountLarry.Text = balanceLarry.ToString("C2");

        }
    }
}
