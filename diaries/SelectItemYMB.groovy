package actions.yamibuy;

import actions.selenium.*


class SelectItem{
    public void run(def params){
        new Click().run("ID":"//a[@href='https://www.yamibuy.com/zh/p/liuzhou-guangxi-specialty-luosifen-pickle-flavor-noodles-280g-no-quail-egg-random-version/1021006541']","ID Type":"XPath")
        ArrayList<String> tabs = new ArrayList<String> (Browser.Driver.getWindowHandles())
        Browser.Driver.switchTo().window(tabs.get(tabs.size()-1))
    }
}