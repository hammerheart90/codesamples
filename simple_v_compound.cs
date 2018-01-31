using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnDetermine_Click(object sender, EventArgs e)
        {
            double principal = 1000;
            double simple, compound;
            lstOutput.Items.Add("YEAR" + "   " + "SIMPLE INTEREST" + "  " + "COMPOUND INTEREST");
            simple = principal;
            compound = principal;
            for (int years = 1; years <= 9; years++)
            {
                simple = simple + 50;
                compound = compound * 1.05;
                lstOutput.Items.Add(years + "            " + simple.ToString("C2") + "                 " + compound.ToString("C2"));
            }
        }
    }
}
