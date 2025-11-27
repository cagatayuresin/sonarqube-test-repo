# SonarQube Demo Repository

[![Quality Gate Status](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=alert_status&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Security Hotspots](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=security_hotspots&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Reliability Issues](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=software_quality_reliability_issues&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Maintainability Issues](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=software_quality_maintainability_issues&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Security Issues](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=software_quality_security_issues&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Maintainability Rating](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=software_quality_maintainability_rating&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Technical Debt](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=software_quality_maintainability_remediation_effort&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)[![Lines of Code](https://sonarqube.cagatayuresin.com/api/project_badges/measure?project=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a&metric=ncloc&token=sqb_3e30436464e87761e0fb365437903cae1bd3a305)](https://sonarqube.cagatayuresin.com/dashboard?id=cagatayuresin_sonarqube-test-repo_1711c38a-25bb-434a-b3c8-c2a13cdc393a)

Bu repository, SonarQube kod kalitesi ve güvenlik analizi sunumu için hazırlanmış kapsamlı bir test reposudur.

## 📋 İçerik

Bu repository, SonarQube'ün tespit edebileceği **tüm issue tiplerini** göstermek için kasıtlı olarak hatalı yazılmış kod örnekleri içerir:

- `BadCode.cs` - C# örnekleri
- `bad_code.py` - Python örnekleri
- `BadCode.java` - Java örnekleri
- `badCode.js` - JavaScript örnekleri

## 🎯 Amaç

SonarQube'ün aşağıdaki tespit yeteneklerini göstermek:

### 🔴 Security Vulnerabilities (Güvenlik Açıkları)

- SQL Injection
- Command Injection
- Hardcoded Credentials
- Weak Cryptography (MD5, SHA1)
- Path Traversal
- Insecure Deserialization
- XSS (Cross-Site Scripting)
- Code Injection (eval, exec)

### 🟡 Code Smells (Kod Kokuları)

- Cognitive Complexity
- Too Many Parameters
- Duplicate Code
- Magic Numbers
- Long Methods
- God Classes
- Empty Catch Blocks
- Unused Variables

### 🔵 Bugs (Hatalar)

- Null Pointer Exceptions
- Division by Zero
- Resource Leaks
- Infinite Loops
- Dead Code
- Array Index Out of Bounds
- Incorrect Exception Handling

### 🟠 Security Hotspots

- Insecure Random Number Generation
- Cookie Security
- HTTP Requests
- File Permissions

## 🚀 Kullanım

### SonarCloud ile (Önerilen)

1. [SonarCloud](https://sonarcloud.io) hesabı oluşturun
2. Repository'yi GitHub App ile bağlayın
3. Otomatik analiz başlayacaktır

### SonarQube Server ile

1. SonarQube Server kurulumu yapın
2. Proje oluşturun
3. Token alın
4. Aşağıdaki komutu çalıştırın:

```bash
sonar-scanner \
  -Dsonar.projectKey=sonarqube-test-repo \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=YOUR_TOKEN
```

### GitHub Actions ile

`.github/workflows/sonarqube.yml` dosyası ekleyerek otomatik CI/CD entegrasyonu yapabilirsiniz.

## 📊 Beklenen Sonuçlar

Bu repository tarandığında SonarQube şunları gösterecektir:

- **100+** Code Smells
- **50+** Bugs
- **30+** Vulnerabilities
- **20+** Security Hotspots
- **F** veya **E** Quality Gate skoru

## ⚠️ UYARI

Bu kod örnekleri **eğitim amaçlıdır** ve kasıtlı olarak hatalıdır. **Asla production ortamında kullanmayın!**

## 📚 Kaynaklar

- [SonarQube Dokümantasyonu](https://docs.sonarqube.org/)
- [SonarCloud](https://sonarcloud.io)
- [SonarQube Rules](https://rules.sonarsource.com/)

## 📝 Lisans

MIT License - Detaylar için `LICENSE` dosyasına bakın.

---

**Not:** Bu repository sadece SonarQube demo ve eğitim amaçlıdır.
