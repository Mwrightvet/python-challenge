{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "budget_data = os.path.join(\"budget_data.csv\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I've read the CSV! Good Job!\n",
      "Skipped header: ['Date', 'Profit/Losses']\n",
      "Total Months: 86\n",
      "Total Profit: $ 38382578.0\n"
     ]
    }
   ],
   "source": [
    "#total number of months included in the dataset\n",
    "total_months = 0\n",
    "#net total amount of \"Profit/Losses\" over the entire period\n",
    "total_amount = 0\n",
    "#average of the changes in \"Profit/Losses\" over the entire period\n",
    "average_change = []\n",
    "#greatest increase in profits (date and amount) over the entire period\n",
    "#average_change = int(budget_data[2])\n",
    "\n",
    "\n",
    "\n",
    "with open(budget_data, newline=\"\") as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "\n",
    "    print(\"I've read the CSV! Good Job!\")\n",
    "    \n",
    "    header = next(csvreader)\n",
    "    \n",
    "    print(\"Skipped header:\", header)\n",
    "    \n",
    "       \n",
    "    for row in csvreader:\n",
    "        #print (row[0])\n",
    "        #add to total_month \n",
    "        total_months += 1\n",
    "        total_amount += float(row[1])\n",
    "        \n",
    "    print(\"Total Months:\" , total_months)\n",
    "    print(\"Total Profit: $\" , total_amount)    \n",
    "#net total amount of \"Profit/Losses\" over the entire period\n",
    "#average of the changes in \"Profit/Losses\" over the entire period\n",
    "#greatest increase in profits (date and amount) over the entire period\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "total_months"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
