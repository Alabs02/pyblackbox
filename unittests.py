import time
import unittest
import pandas as pd
import unittest
from subprocess import call
import tkinter as tk 

from Test import openCovid

class MyGUI(tkinter.Frame):
    def __init__(self, master, **kw):
        tkinter.Frame.__init__(self, master, **kw)
        self.info_button = tkinter.Button(self, command=self.info_cmd, text='Info')
        self.info_button.pack()
        self.quit_button = tkinter.Button(self, command=self.quit_cmd, text='Quit')
        self.quit_button.pack()

    def info_cmd(self):
        messagebox.showinfo('Info', master=self)

    def quit_cmd(self):
        confirm = messagebox.askokcancel('Quit?', master=self)
        if confirm:
            self.destroy()


class TKinterTestCase(unittest.TestCase):
    def setUp(self):
        self.root = tkinter.Tk()
        self.root.bind('<Key>', lambda e: print(self.root, e.keysym))

    def tearDown(self):
        if self.root:
            self.root.destroy()

    def test_enter(self):
        v = MyGUI(self.root)
        v.pack()
        self.root.update_idletasks()

        # info
        v.after(100, lambda: self.root.event_generate('<Return>'))
        v.info_button.invoke()

        # quit
        def cancel():
            self.root.event_generate('<Tab>')
            self.root.event_generate('<Return>')

        v.after(100, cancel)
        v.quit_button.invoke()
        self.assertTrue(v.winfo_ismapped())    
        v.after(100, lambda: self.root.event_generate('<Return>'))
        v.quit_button.invoke()
        with self.assertRaises(tkinter.TclError):
            v.winfo_ismapped()


if __name__ == "__main__":
    unittest.main()

start_time = time.perf_counter()

call(["python", "Test.py"])


end_time = time.perf_counter()

elapsed_time = end_time - start_time

print("Time elapsed: {:.2f} seconds".format(elapsed_time))

#opencpvid test


def test_openCovid_window(self):
    openCovid()
    self.assertIsInstance(covidWindow, tk.Tk)
    self.assertEqual(covidWindow.geometry(), '500x500')

#total daily cases

def test_openCovid_totalDailyCases(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsNotNone(covidData)




#sum covid data

def test_openCovid_sumCovidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsInstance(sumCovidData, pd.Series)
        self.assertEqual(sumCovidData.name, 'Total number of cases daily')

#Test Covid data 

def test_openCovid_cleanCovidData_date(self):
    with patch('builtins.input', return_value='test_file.csv'):
        openCovid()
        self.assertIsInstance(cleanCovidData['Month'], pd.Series)
        self.assertIsInstance(cleanCovidData['Week'], pd.Series)
        self.assertIsInstance(cleanCovidData['Day'], pd.Series)


#open_file function 

def test_changeInCasesOverTimeAndLocation_open_file(self):
    with patch('builtins.input', return_value='test_file.csv'):
        with patch('tk.filedialog.askopenfile', return_value='test_file.csv'):
            changeInCasesOverTimeAndLocation()

#Test that the covidData DataFrame is created correctly:
def test_changeInCasesOverTimeAndLocation_covidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        with patch('tk.filedialog.askopenfile', return_value='test_file.csv'):
            changeInCasesOverTimeAndLocation()
            self.assertIsInstance(covidData, pd.DataFrame)
            self.assertEqual(covidData.index.name, 'date')

#Test that the cleanCovidData DataFrame is created correctly:


def test_changeInCasesOverTimeAndLocation_cleanCovidData(self):
    with patch('builtins.input', return_value='test_file.csv'):
        with patch('tk.filedialog.askopenfile', return_value='test_file.csv'):
            changeInCasesOverTimeAndLocation()
            self.assertIsInstance(cleanCovidData, pd.DataFrame)
           
#



class TestCompareAreas(unittest.TestCase):
    def test_compare_areas(self):
        # Arrange
        file_contents = '''date,newCasesBySpecimenDate-0_4,newCasesBySpecimenDate-0_59
2022-01-01,1,2
2022-01-02,3,4
2022-01-03,5,6'''
        expected_output = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=['newCasesBySpecimenDate-0_4', 'newCasesBySpecimenDate-0_59'], index=[0, 1, 2])

        # Act
        result = compareAreas(file_contents)

        # Assert
        self.assertEqual(result.shape, expected_output.shape)
        pd.testing.assert_frame_equal(result, expected_output)

class TestCompareAreasCumulativeSum(unittest.TestCase):

    def test_open_file(self):
        # mock the filedialog.askopenfile() function
        # to return a known file object
        with mock.patch('filedialog.askopenfile', return_value=mock_file):
            file7 = compareAreasCumulativeSum.open_file()
            # check that the function correctly assigns the file object
            self.assertEqual(file7, mock_file)


class TestOpenStopnSearch(unittest.TestCase):

    def test_api_requests(self):
        # mock the urllib.request.urlopen() function
        # to return known responses
        with mock.patch('urllib.request.urlopen', side_effect=[mock_response1, mock_response2]):
            openStopnSearch.showClevelandNorthumbriaOutcome()
            # check that the function correctly assigns the data to the variables
            self.assertEqual(openStopnSearch.clevelandData, mock_response1.read())
            self.assertEqual(openStopnSearch.northumbriaData, mock_response2.read())


class TestGetUrl(unittest.TestCase):

    def test_url_construction(self):
        area_string = "northumbria"
        date_obj = "2021-06"
        expected_url = "https://data.police.uk/api/stops-force?force=northumbria&date=2021-06"
        # call the getUrl() function and check if it returns the correct URL
        self.assertEqual(getUrl(area_string, date_obj), expected_url)



def test_showBreakdownAcrossYears():
    # mock the getUrl function to return a fixed url for testing
    with patch("openStopnSearch.getUrl") as mock_getUrl:
        mock_getUrl.return_value = "https://mock.url"

        # mock the urllib.request.urlopen function to return a mock response
        # that can be used to generate the pandas dataframes
        with patch("urllib.request.urlopen") as mock_urlopen:
            mock_response_2021 = mock_open(read_data=b'{"age_range": "20-24", "gender": "M"}')
            mock_response_2020 = mock_open(read_data=b'{"age_range": "25-29", "gender": "F"}')
            mock_urlopen.side_effect = [mock_response_2021, mock_response_2020]

            # call the function being tested
            showBreakdownAcrossYears()

            # assert that getUrl was called with the correct arguments
            mock_getUrl.assert_any_call("northumbria", "2021-03")
            mock_getUrl.assert_any_call("northumbria", "2020-04")

            # assert that urlopen was called with the correct url
            mock_urlopen.assert_any_call("https://mock.url")

            # assert that the pandas dataframes were created with the correct data
            assert northumbria2021Dataset.loc[0, "age_range"] == "20-24"
            assert northumbria2020Dataset.loc[0, "age_range"] == "25-29"
            assert northumbria2021Dataset.loc[0, "gender"] == "M"
            assert northumbria2020Dataset.loc[0, "gender"] == "F"

