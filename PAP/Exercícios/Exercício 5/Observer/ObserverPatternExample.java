import java.util.ArrayList;
import java.util.List;

interface WeatherObserver {
    void update(String weatherUpdate);
}

interface Subject {
    void addObserver(WeatherObserver observer);
    void removeObserver(WeatherObserver observer);
    void notifyObservers();
}

class WeatherService implements Subject {
    private List<WeatherObserver> observers = new ArrayList<>();
    private String weatherCondition;

    public void addObserver(WeatherObserver observer) {
        observers.add(observer);
    }

    public void removeObserver(WeatherObserver observer) {
        observers.remove(observer);
    }

    public void notifyObservers() {
        for (WeatherObserver observer : observers) {
            observer.update(weatherCondition);
        }
    }

    public void setWeatherCondition(String newCondition) {
        this.weatherCondition = newCondition;
        System.out.println("\n[WeatherService] Nova condição do tempo: " + newCondition);
        notifyObservers();
    }
}

class PhoneWidget implements WeatherObserver {
    private String name;

    public PhoneWidget(String name) {
        this.name = name;
    }

    @Override
    public void update(String weatherUpdate) {
        System.out.println("[Celular - " + name + "] Notificação: O clima mudou para: " + weatherUpdate);
    }
}

class NotebookWidget implements WeatherObserver {
    @Override
    public void update(String weatherUpdate) {
        System.out.println("[Notebook Widget] Atualizando tela: " + weatherUpdate);
    }
}

class SmartTV implements WeatherObserver {
    @Override
    public void update(String weatherUpdate) {
        System.out.println("[Smart TV] Exibindo notificação: " + weatherUpdate);
    }
}

class AlexaAssistant implements WeatherObserver {
    @Override
    public void update(String weatherUpdate) {
        System.out.println("[Alexa] Dizendo: 'Atenção, o clima mudou para " + weatherUpdate + ".'");
    }
}

// Novo Observador - Painel Digital de Rua
class StreetPanel implements WeatherObserver {
    @Override
    public void update(String weatherUpdate) {
        System.out.println("[Painel Digital de Rua] Exibindo no painel: " + weatherUpdate);
    }
}

public class ObserverPatternExample {
    public static void main(String[] a) {
        WeatherService weatherService = new WeatherService();
        PhoneWidget phone = new PhoneWidget("Ricardo");
        NotebookWidget notebook = new NotebookWidget();
        SmartTV tv = new SmartTV();
        AlexaAssistant alexa = new AlexaAssistant();
        StreetPanel painel = new StreetPanel(); // Novo observador

        weatherService.addObserver(phone);
        weatherService.addObserver(notebook);
        weatherService.addObserver(tv);
        weatherService.addObserver(alexa);
        weatherService.addObserver(painel); // Adicionando o novo observador

        weatherService.setWeatherCondition("Chuva forte");
        weatherService.setWeatherCondition("Ensolarado com ventos fracos");
    }
}
