import  pytest
import allure
import yaml
from yaml_demo import WRYaml
from core.cal import Cal
from tests.contest import calc_init

# def load_data(path='data.yaml'):
#     with open(path) as f:
#         data=yaml.safe_load(f)
#         keys=','.join(data[0].keys())
#         values=[d.values() for d in data]
#         data={'keys':keys,'values':values}
#         print(data)
#         print(keys)
#         print(values)
#         return data
@allure.feature('算法模块')
class Testcal():
    # data=load_data()
    def setup_class(self):
        self.cal=Cal()
        self.wryaml=WRYaml()

    # data = load_data()
    # @pytest.mark.parametrize('a,b,c',[(5,2,3),(8,2,6),(1,2,9)])
    def get_data(self):
        data1 = self.wryaml.read_yaml('conf.yaml')
        lis = [i['a'] for i in data1]
        return lis
    @allure.story('加法测试用例')
    @pytest.mark.parametrize('a,b,c',[(2,1,2),(0.2,0.1,2),(2,0.2,0.0)])
    def test_sub(self,a,b,c):
        assert self.cal.sub(a,b)==c
        #正常值计算
    @allure.story('除法测试用例')
    @pytest.mark.parametrize('a,b,c',[(2,1,2),(0.2,0.1,2),(2,0.2,0.0)])
    def test_div(self,a,b,c):
        assert self.cal.div(a,b)==c
        #异常值计算
    @pytest.mark.parametrize('a,b',[(1,0),(0.2,0)])
    @allure.story('除法测试用例')
    def test_div(self,a,b):
        with allure.step('除数为0'):
            print("除数为0")
        with pytest.raises(ZeroDivisionError):
            assert self.cal.div(a,b)

    def test_add(self,calc_init):
        assert  calc_init.add(2,1)==3
if __name__ == '__main__':
    Testcal=Testcal()
    print(Testcal.get_data())
